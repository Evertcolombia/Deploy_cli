#!/bin/env python3

from commands.controllers.create_connection import create_connection
from commands.modules.portainer_service import init_portainer_service
from commands.controllers.init_service import init_service

from typer import Argument, Typer, colors, echo, style

app = Typer()

@app.command()
def service(ip: str = Argument(..., help="Server IP"),
        key_ssh: str = Argument(..., help="Path to SSH key file"),
        user_ssh: str = Argument(..., help="Server User"),
        host: str = Argument(..., help="hostname for the server"),):
    """
        Portainer user interface allows you to see
        the state of your Docker services in a Docker
        Swarm mode cluster and manage it.
    """
    server = create_connection(user_ssh, ip, key_ssh)
    init_service(host, server)
    domain = init_portainer_service(server)
    entire_domain = 'https://{}'.format(domain)
    echo(style(entire_domain, fg=colors.BLUE, bold=True))
