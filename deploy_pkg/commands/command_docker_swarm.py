#!/bin/env python3

from commands.modules.create_connection import create_connection
from commands.modules.init_swarm import init_swarm
from typing import Optional

import typer

app = typer.Typer()
blue = typer.colors.BLUE
red = typer.colors.RED


@app.command()
def swarm(ip: str = typer.Argument(...),
            key_ssh: str = typer.Argument(..., help="Path to ssh key file"),
            user_ssh: str = typer.Argument(..., help="User to use in serve"),
            hostname: str = typer.Argument(..., help="Ex: ws01.example.com"),
            swarm_mode: Optional[bool] = False
):
    """Init Swarm Mode"""
    if swarm_mode:
        server = create_connection(user_ssh, ip, key_ssh)
        nt = init_swarm(server, hostname)
        msg = typer.style("Manager Node Token: {}".format(nt), fg=blue, bold=True)
        typer.echo(msg)
    else:
        typer.echo(typer.style("--swarm-mode must be set", fg=red, bold=True))
        exit(0)
