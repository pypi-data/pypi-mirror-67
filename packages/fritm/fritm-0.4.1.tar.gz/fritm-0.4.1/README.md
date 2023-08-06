# FRida In The Middle

`fritm` is a minimalist, cross-platform (tested on macOS and Windows)
network reverse engineering framework written in Python.

`fritm-hook` allows you to easily hook the
[`connect()`](http://man7.org/linux/man-pages/man2/connect.2.html)
function with [`frida`](https://www.frida.re/) to redirect all traffic
from a target application.

You can then use the builtin server written in Python to initiate a
[Man-in-the-middle
attack](https://en.wikipedia.org/wiki/Man-in-the-middle_attack).

Even if you don't want to use Python, you can use the `fritm-hook`
command to redirect the traffic to your application and implement the
simple lecture of the `HTTP CONNECT` header.

## Installation

``` bash
pip install fritm
```

## Usage

Hook the process:

``` bash
fritm-hook PROCESS_NAME_OR_PID -p PORT # (default 8080)
```

Or create a new one:

``` bash
fritm-spawn PATH_TO_COMMAND -p PORT # (default 8080)
```

Launch a proxy server in Python:

``` python
import select

from fritm import start_proxy_server


def dumb_callback(soClient, soServer):
    """Forwards all the traffic between the two sockets
    """
    conns = [soClient, soServer]
    other = {soClient: soServer, soServer: soClient}
    active = True
    try:
        while active:
            rlist, wlist, xlist = select.select(conns, [], conns)
            if xlist or not rlist:
                break
            for r in rlist:
                data = r.recv(8192)
                if not data:
                    active = False
                    break
                other[r].sendall(data)
    finally:
        for c in conns:
            c.close()

httpd = start_proxy_server(dumb_callback)
```

Now, all the traffic will go through your application. You can modify
anything on the fly.

## How does it work?

### Hooking with `fritm.hook(process, port, filter)`

1.  attach to the target process
2.  intercept the calls to
    [`connect()`](http://man7.org/linux/man-pages/man2/connect.2.html)
3.  replace the target IP address by 127.0.0.1 and the port with the
    chosen one
4.  execute the `connect()` function with the local IP
5.  just before returning, send the [HTTP CONNECT
    method](https://en.wikipedia.org/wiki/HTTP_tunnel#HTTP_CONNECT_method)
    with the original IP and port

`fritm.spawn_and_hook(process, port)` launches the process and ensures
it is hooked from the beginning.

### MITM with `fritm.start_proxy_server(callback, port, filter)`

1.  Launch a local server that listens for connections on the given port
2.  Upon receiving a new connection from the hooked client, read the IP
    and port of the server from the HTTP CONNECT header
3.  Open a new socket to the server
4.  Call `callback(socket_to_client, socket_to_server)`


### `filter` usage

When specified, `filter` allows you to not redirect some connections.
It is a javascript expression that can use the variables `sa_family`,
`addr` and `port`.
A good value is `sa_family == 2` (corresponds to `AF_INET` aka ipv4), but
for unknown reasons `sa_family` is 0 on Windows.

 
## Differences with [mitmproxy](https://mitmproxy.org/)

  - mitmproxy doesn't use function hooking, it intercepts all the
    traffic from your browser or computer
  - mitmproxy only works for HTTP traffic, whereas fritm works with any
    TCP
traffic.

## Differences with [proxychains](https://github.com/haad/proxychains) / [proxychains-ng](https://github.com/rofl0r/proxychains-ng)

  - `fritm-spawn` is intented as simplified and cross-platform version
    of proxychains.
  - `fritm-hook` can attach to an already running process.
  - proxychains is not cross-platform and hard to install, whereas fritm
    is cross-platform and simple to install.
  - proxychains uses a config file whereas `fritm-spawn` only takes two
    arguments
  - fritm includes a HTTP proxy server (that is also able to communicate
    with proxychains)
  - proxychains can handle a lot of different proxy types (SOCKS4,
    SOCKS5, HTTPS) with a lot of options (e.g. for authentification)
  - proxychains can chain multiple proxies
  - proxychains handles any proxy address whereas `fritm-spawn` defaults
    to localhost. However, if anyone needs it for remote addresses, post
    an issue and I'll implement it.

## Current limitations

  - Some Windows user faced issues that I couldn't reproduce
  - fritm will fail on IPv6 addresses, but it should not be hard to fix
    (I just don't happen to have any application that uses an IPv6
    address to test).
