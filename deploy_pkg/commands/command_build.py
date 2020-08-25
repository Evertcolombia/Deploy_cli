#!/usr/bin/env python3
from commands.modules.create_connection import create_connection
from commands.modules.init_swarm import init_swarm
from commands.modules.install_docker import install_docker
from commands.modules.install_docker_compose import install_docker_compose
from typing import Optional

import typer

app = typer.Typer()


@app.command()
def hello(
            # ip: str = typer.Argument(...),
            # key_ssh: str = typer.Argument(...),
            # user_ssh: str = typer.Argument(...),
            ip: str = typer.Option(...),
            key_ssh: str = typer.Option(...),
            user_ssh: str = typer.Option(...),
            swarm_mode: Optional[bool] = False
):
    """yummy"""
    server = create_connection(user_ssh, ip, key_ssh)
    install_docker(server)
    install_docker_compose(server)
    if swarm_mode:
        node_token = init_swarm(server)
        typer.echo("Manager Node token : {}".format(node_token))
