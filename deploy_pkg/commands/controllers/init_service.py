#!/bin/env python3

import os
import socket

import paramiko
from typer import colors, echo, style

from commands.controllers.create_file import init_service_file

blue = colors.BLUE
red = colors.RED

def init_service(host: str, server):
    try:
        path = os.getcwd() + '/commands/modules/init_service.sh'
        init_service_file(host, path)
        server.put(path, '.')
        echo(style("Update server and hostname", fg=blue, bold=True))
        server.run("bash init_service.sh")
    except socket.error:
        echo(style('unable to connect', fg=red, bold=True))
        exit(0)
    except paramiko.ssh_exception.AuthenticationException:
        echo(style("SSH Error, verify the key path", fg=red))
        exit(0)
