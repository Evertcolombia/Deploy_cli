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
            key_ssh: str = typer.Argument(...),
            user_ssh: str = typer.Argument(...),
            hostname: str = typer.Argument(...),
            swarm_mode: Optional[bool] = False
):
    """Init Swarm Mode"""
    if swarm_mode:
        server = create_connection(user_ssh, ip, key_ssh)
        node_token = init_swarm(server, hostname)
        msg = typer.style("Manager Node Token: {}".format(node_token), fg=blue, bold=True)
        typer.echo(msg)
    else:
        typer.style(typer.echo("--swarm_mode must be set"), fg=red, bold=True)
