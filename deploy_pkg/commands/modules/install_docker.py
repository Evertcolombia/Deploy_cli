#!/usr/bin/env python3
import socket

import paramiko
import typer
from colored import fg, stylize

blue = typer.colors.BLUE
red = typer.colors.RED

def install_docker(server):
    try:
        server.run('docker -v')
    except:
        try:
            msg = typer.style("The server is being update", fg=blue, bold=True)
            typer.echo(msg)
            server.run('sudo apt-get update')
            server.run('sudo apt-get upgrade -y')
            typer.echo(typer.style("Install Docker", fg=blue, bold=True))
            server.run('curl -fsSL get.docker.com -o get-docker.sh')
            server.run('CHANNEL=stable sh get-docker.sh')
            server.run('rm get-docker.sh')
        except socket.error:
            typer.echo(typer.style("Unable to connect", fg=red))
            exit(0)
        except paramiko.ssh_exception.AuthenticationException:
            typer.echo(typer.style("SSH Error, verify kay path", fg=red))
            exit(0)
