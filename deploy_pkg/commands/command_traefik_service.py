#!/usr/bin/env python3
from commands.modules.create_connection import create_connection
from commands.modules.init_service import init_service
from commands.modules.init_traefik_service import init_traefik_service

import typer

app = typer.Typer()

blue = typer.colors.BLUE

@app.command()
def service(
    ip: str = typer.Argument(...),
    key_ssh: str = typer.Argument(...),
    user_ssh: str = typer.Argument(...),
    host: str = typer.Argument(...),
):
    """Create traefik load balancer/proxy service"""
    server = create_connection(user_ssh, ip, key_ssh)
    init_service(host, server)
    domain = init_traefik_service(server)
    entire_domain = 'https://{}'.format(domain)
    msg = typer.style(entire_domain, fg=blue, bold=True)
    typer.echo(msg)
