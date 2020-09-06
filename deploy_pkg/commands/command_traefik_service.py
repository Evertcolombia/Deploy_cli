#!/bin/env python3
from commands.controllers.create_connection import create_connection
from commands.controllers.init_service import init_service
from commands.modules.traefik_service import init_traefik_service

from typer import Argument, Typer, colors, echo, style

app = Typer()


@app.command()
def service(
    ip: str = Argument(..., help='Server IP'),
    key_ssh: str = Argument(..., help='SHH file path'),
    user_ssh: str = Argument(..., help='Server user'),
    host: str = Argument(..., help='Server name domain'),
):
    """Create traefik load balancer/proxy service"""
    server = create_connection(user_ssh, ip, key_ssh)
    init_service(host, server)
    domain = init_traefik_service(server)
    entire_domain = 'https://{}'.format(domain)
    echo(style(entire_domain, fg=colors.BLUE, bold=True))
