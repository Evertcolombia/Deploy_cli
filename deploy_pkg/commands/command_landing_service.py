#!/usr/bin/python3

from commands.controllers.create_connection import create_connection
from commands.modules.landing_service import landing_service
from commands.controllers.init_service import init_service

from typer import Argument, colors, echo, style, Typer

app = Typer()

@app.command()
def service(ip: str = Argument(..., help='Server IP'),
        key_ssh: str = Argument(..., help="Path to SSH key file"),
        user_ssh: str = Argument(..., help="Server User"),
        host: str = Argument(..., help="hostname for the server")
):
    """
        Launch you own landing page service
    """
    server = create_connection(user_ssh, ip, key_ssh)
    init_service(host, server)
    domain = landing_service(server)
    entire_domain = 'https://{}'.format(domain)
    echo(style(entire_domain, fg=colors.BLUE, bold=True))
