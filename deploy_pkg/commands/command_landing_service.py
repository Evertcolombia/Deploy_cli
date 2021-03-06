#!/usr/bin/python

from commands.controllers.create_connection import create_connection
from commands.controllers.init_service import init_service
from commands.modules.landing_service import landing_service

from typer import Argument, Typer, colors, echo, style

app = Typer()

@app.command()
def service(ip: str = Argument(..., help='Server IP'),
        key_ssh: str = Argument(..., help="Path to SSH key file"),
        user_ssh: str = Argument(..., help="Server User"),
        host: str = Argument(..., help="hostname for the server"),
        dir_path: str = Argument(..., help="Path to the landing folder")
):
    """
        Launch you own landing page service
    """
    server = create_connection(user_ssh, ip, key_ssh)
    #init_service(host, server)
    domain = landing_service(server, dir_path)
    entire_domain = 'https://{}'.format(domain)
    echo(style(entire_domain, fg=colors.BLUE, bold=True))
