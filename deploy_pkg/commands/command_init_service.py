#!/usr/bin/env python3
from commands.modules.create_connection import create_connection
from commands.modules.init_service import init_service
from commands.modules.init_traefik_service import init_traefik_service

import typer

app = typer.Typer()

@app.command()
def service(
    ip: str = typer.Argument(...),
    key_ssh: str = typer.Argument(...),
    user_ssh: str = typer.Argument(...),
    host: str = typer.Argument(...),
    domain: str = typer.Argument(...),
    username: str = typer.Argument(...),
    email: str = typer.Argument(...),
    password: str = typer.Argument(...)
):
    """Create traefik load balancer/proxy service"""
    server = create_connection(user_ssh, ip, key_ssh)
    init_service(host, server)
    print("HEREE")
    print(email + ' ' + domain + ' ' + username + ' ' + password)
    init_traefik_service(server, username, password, email, domain)
    msg = typer.style('canaccess the web https://traefik.<your domain>', fg=typer.colors.BLUE, bold=True)
    typer.echo(msg)
