#!/usr/bin/python

import os
from commands.controllers.create_connection import create_connection
from commands.controllers.create_file import app_data_file
from commands.controllers.run_app import run_app
from commands.controllers.setup_github import make_clone, setup_git

from typer import Argument, Typer, colors, echo, style

app = Typer()


@app.command()
def service(ip: str = Argument(..., help='Server IP'),
        key_ssh: str = Argument(..., help='Path to SSH key file'),
        user_ssh: str = Argument(..., help='Server User')):

    """
        Send directory with your app to the server
        and run services
    """
    path = os.getcwd()
    if '/deploy_pkg' in path:
        path = path + '/commands/templates/app_file.sh'
    else:
        path = path + '/deploy_pkg/commands/templates/app_file.sh'

    server = create_connection(user_ssh, ip, key_ssh)
    git_path = setup_git(server)
    make_clone(server, git_path)
    app_data_file(path)
    run_app(server, path)
