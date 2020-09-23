#!/usr/bin/python
import socket

import paramiko
from typer import colors, echo, style

blue = colors.BLUE
red = colors.RED


def install_docker(server):
    try:
        server.run('docker -v')
    except:
        try:
            echo(style("The server is being updateeeee", fg=blue, bold=True))
            server.run('sudo apt-get update -y')
            server.run('sudo apt-get upgrade -y')
            echo(style("Install Docker", fg=blue, bold=True))
            server.run('curl -fsSL get.docker.com -o get-docker.sh')
            server.run('CHANNEL=stable sh get-docker.sh')
            server.run('rm get-docker.sh')
        except socket.error:
            echo(style("Unable to connect", fg=red, bold=True))
            exit(0)
        except paramiko.ssh_exception.AuthenticationException:
            echo(style("SSH Error, verify kay path", fg=red, bold=True))
            exit(0)
