#!/usr/bin/python

import socket

import paramiko
import typer
from typer import colors, echo, style


blue = colors.BLUE
red = colors.RED

def install_docker_compose(server):
    try:
        server.run('docker-compose -v')
    except:
        try:
            echo(style("Install docker-compose", fg=blue, bold=True))
            server.run('sudo curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
            server.run('sudo chmod +x /usr/local/bin/docker-compose')
        except socket.error:
            echo(style("Unable to connect", fg=red, bold=True))
            exit(0)
        except paramiko.ssh_exception.AuthenticationException:
            echo(style("SSH Error, verify the kay path", fg=red, bold=True))
            exit(0)
