#!/usr/bin/env python3
from commands.modules.create_connection import create_connection
from commands.modules.install_docker import install_docker
from commands.modules.install_docker_compose import install_docker_compose

import typer

app = typer.Typer()


@app.command()
def setUp(
            ip: str = typer.Argument(...),
            key_ssh: str = typer.Argument(...),
            user_ssh: str = typer.Argument(...),
):
    """Create connection"""
    server = create_connection(user_ssh, ip, key_ssh)
    install_docker(server)
    install_docker_compose(server)
