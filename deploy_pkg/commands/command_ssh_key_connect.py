#!/bin/env/python3

from commands.controllers.ssh_config import init_ssh_keys
from os import getcwd, system

from typer import Argument, Typer, colors, echo, prompt, style

app = Typer()


@app.command()
def keygen(key_name: str = Argument(..., help="SSH key name"),
    user: str = Argument(..., help="User in the server"),
    ip: str = Argument(..., help="Server IP"),
    bit: str = Argument(..., help="bits number in the new key can be 1024 - 4096")):
    if int(bit) < 1094 and int(bit) > 4096:
        bit = '2048'
    try:
        init_ssh_keys(key_name, user, ip, bit)
    except:
        system('rm $HOME/{}'.format(key_name))
        system('y')
        msg = "Cant complete the service, out now"
        echo(style(msg, fg=colors.RED, bold=True))
        exit(0)
