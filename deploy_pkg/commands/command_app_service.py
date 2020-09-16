#!/usr/bin/python

import os
from commands.controllers.create_connection import create_connection
from commands.controllers.create_file import app_data_file
from commands.deploy.deploy_app_service import deploy
from commands.controllers.run_app import run_app

from typer import Argument, Typer, colors, echo, style

app = Typer()


@app.command()
def service(ip: str = Argument(..., help='Server IP'),
        key_ssh: str = Argument(..., help='Path to SSH key file'),
        user_ssh: str = Argument(..., help='Server User'),
        dir_path: str = Argument(..., help='Folder path')):
    """
        Send directory with your app to the server
        and run services
    """
    path = os.getcwd() + '/commands/templates/app_file.sh'
    server = create_connection(user_ssh, ip, key_ssh)
    deploy(server, dir_path)
    app_data_file(path)
    run_app(server, path)
