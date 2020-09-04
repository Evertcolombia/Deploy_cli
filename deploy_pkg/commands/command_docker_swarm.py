#!/bin/env python3

from commands.modules.create_connection import create_connection
from commands.modules.init_swarm import init_swarm
from typing import Optional

from typer import Argument, Typer, colors, echo, style

app = Typer()
blue = colors.BLUE
red = colors.RED


@app.command()
def swarm(ip: str = Argument(..., help="Server IP"),
        key_ssh: str = Argument(..., help="Path to ssh key file"),
        user_ssh: str = Argument(..., help="User to use in serve"),
        hostname: str = Argument(..., help="Ex: ws01.example.com"),
        swarm_mode: Optional[bool] = False
):
    """Init Swarm Mode"""
    if swarm_mode:
        server = create_connection(user_ssh, ip, key_ssh)
        n_tkn = init_swarm(server, hostname)

        echo(style("Manager NodeToken: {}".format(n_tkn), fg=blue, bold=True))
    else:
        echo(style("--swarm-mode must be set", fg=red, bold=True))
        exit(0)
