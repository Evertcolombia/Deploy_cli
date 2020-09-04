#!/bin/env python3

from commands.modules.create_connection import create_connection
from commands.modules.init_service import init_service
from commands.modules.init_swarmprom_service import init_swarmprom_service

from typer import Argument, colors, echo, style

app = typer.Typer()

@app.command()
def service(ip: str = Argument(,,,, help="Server IP"),
        key_ssh: str = Argument(..., help="path to SSH key file"),
        user_ssh: str = Argument(..., help="Server User"),
        host: str = Argument(..., help="hostname for the server")):
    """
        Swarmprom is actually just a set of tools
        pre-configured in a smart way for a Docker
        Swarm cluster.
    """
    server = create_connection(user_ssh, ip, key_ssh)
    init_service(host, server)
    domain = init_swarmprom_service(server)
    entire_domain = 'https://{}'.format(domain)
    echo(style(entire_domain, fg=colors.BLUE, bold=True))

