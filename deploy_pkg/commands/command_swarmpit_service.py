#!/bin/env python3

from commands.modules.create_connection import create_connection
from commands.modules.init_service import init_service
from commands.modules.init_swarmpit_service import init_swarmpit_service

from typer import Argument, Typer, colors, echo, style

app = Typer()


@app.command()
def service(ip: str = Argument(..., help="Server IP"),
        key_ssh: str = Argument(..., help="Path to SSH key file"),
        user_ssh: str = Argument(..., help="Server User"),
        host: str = Argument(..., help="hostname for the server")):
    """
        Swarmpit provides manner to operate your docker swarm
        clouster with a web user interface
    """
    server = create_connection(user_ssh, ip, key_ssh)
    init_service(host, server)
    domain = init_swarmpit_service(server)
    entire_domain = 'https://{}'.format(domain)
    echo(style(entire_domain, fg=colors.BLUE, bold=True))
