#!/usr/bin/env python3

from pathlib import Path
import sys

import click
import frida

SCRIPT = (Path(__file__).parent / "script.js").read_text()


def spawn_and_hook(program, port=8080):
    pid = frida.spawn(program)
    session = frida.attach(pid)
    script = SCRIPT.replace("8080", str(port))
    frida_script = session.create_script(SCRIPT)
    frida_script.load()
    frida.resume(pid)


def hook(target, port=8080):
    session = frida.attach(target)
    script = SCRIPT.replace("8080", str(port))
    frida_script = session.create_script(SCRIPT)
    frida_script.load()


@click.command(help="Process: Unique name or PID of the process to attach to")
@click.argument("target")
@click.option(
    "-p",
    "--port",
    type=int,
    help="Local port to redirect to",
    default=8080,
    show_default=True,
)
def _main_spawn(target, port):
    spawn_and_hook(target, port)
    if not sys.flags.interactive:
        sys.stdin.read()  # infinite loop


@click.command(help="Process: Unique name or PID of the process to attach to")
@click.argument("target")
@click.option(
    "-p",
    "--port",
    type=int,
    help="Local port to redirect to",
    default=8080,
    show_default=True,
)
def _main_hook(target, port):
    if str.isdigit(target):
        target = int(target)
    hook(target, port)
    if not sys.flags.interactive:
        sys.stdin.read()  # infinite loop
