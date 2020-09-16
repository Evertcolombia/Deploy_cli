#!/usr/bin/python

import os
import socket
from commands.controllers.create_file import swarmpit_data_file

import paramiko
from typer import colors, echo, style

blue = colors.BLUE
red = colors.RED


def init_swarmpit_service(server):
    """
        Setup swarmpit service on node
    """
    try:
        path = os.getcwd() + '/commands/templates/swarmpit_file.sh'
        echo(style("Setting new service", fg=blue, bold=True))
        domain = swarmpit_data_file(path)
        server.put(path, '.')
        server.run('bash swarmpit_file.sh')
        server.run('rm swarmpit_file.sh')
        server.run('docker stack ls')
        return domain
    except socket.error:
        echo(style('unable to connect', fg=red, bold=True))
        exit(0)
    except paramiko.ssh_exception.AuthenticationException:
        echo(style("SSH Error, verify the key path", fg=red, bold=True))
        exit(0)
