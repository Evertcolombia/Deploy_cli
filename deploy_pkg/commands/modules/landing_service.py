#!/usr/bin/python3

import os
import socket
from commands.controllers.create_file import landing_data_file
from commands.deploy.deploy_landing_page import deploy

import paramiko
from typer import colors, echo, style

blue = colors.BLUE
red = colors.RED


def landing_service(server, dir_path):
    """
        sets landing page on domain
    """
    try:
        path = os.getcwd() + '/commands/templates/landing_file.sh'
        print(path)
        echo(style('Setting landing page service', fg=blue, bold=True))
        deploy(server, dir_path)
        domain = landing_data_file(path, dir_path)
        server.put(path, '.')
        server.run('bash landing_file.sh')
        server.run('rm landing_file.sh')
        os.remove(path)
        return domain
    except socket.error:
        echo(style('unable to connect', fg=red, bold=True))
        exit(0)
    except paramiko.ssh_exception.AuthenticationException:
        echo(style("SSH Error, verify the key path", fg=red))
        exit(0)
