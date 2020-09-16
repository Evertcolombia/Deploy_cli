#!/usr/bin/python

import os
import socket
from commands.controllers.create_file import swarmprom_data_file

import paramiko
from typer import colors, echo, style

blue = colors.BLUE
red = colors.RED


def init_swarmprom_service(server):
    """
        setup swarmprom service components
    """
    try:
        path = os.getcwd() + '/commands/templates/swarmprom_file.sh'
        echo(style("Setup Service", fg=blue, bold=True))
        server.run('git clone https://github.com/stefanprodan/swarmprom.git')
        server.run('cd swarmprom')
        domain = swarmprom_data_file(path)
        server.put(path, '.')
        server.run('bash swarmprom_file.sh')
        server.run('rm swarmprom_file.sh')
        #os.remove(path)
        echo(style('Stack list of connected services:', fg=blue, bold=True))
        server.run('docker stack ls')
        echo(style('services that swarmprom provide:', fg=blue, bold=True))
        server.run('docker stack ps swarmprom')
        return domain
    except socket.error:
        echo(style('unable to connect', fg=red, bold=True))
        exit(0)
    except paramiko.ssh_exception.AuthenticationException:
        echo(style("SSH Error, verify the key path", fg=red, bold=True))
        exit(0)
