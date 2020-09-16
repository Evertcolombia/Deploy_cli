#!/usr/bin/python

import os
import socket
from commands.controllers.create_file import portainer_data_file

import paramiko
from typer import colors, echo, style

blue = colors.BLUE
red = colors.RED

def init_portainer_service(server):
    """
        Setup Portainer service
    """
    try:
        path = os.getcwd() + '/commands/templates/portainer_file.sh'
        echo(style("Setup Service", fg=blue, bold=True))
        domain = portainer_data_file(path)
        server.put(path, '.')
        server.run('bash portainer_file.sh')
        server.run('rm portainer_file.sh')
        os.remove(path)
        server.run('docker stack ls')
        server.run('docker stack ps portainer')
        return domain
    except socket.error:
        echo(style('unable to connect', fg=red, bold=True))
        exit(0)
    except paramiko.ssh_exception.AuthenticationException:
        echo(style("SSH Error, verify the key path", fg=red, bold=True))
        exit(0)
