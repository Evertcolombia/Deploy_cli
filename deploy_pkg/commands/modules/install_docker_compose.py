#!/usr/bin/env python3

import socket

import paramiko
import typer

blue = typer.colors.BLUE
red = typer.colors.RED

def install_docker_compose(server):
    try:
        server.run('docker-compose -v')
    except:
        try:
            msg = typer.style("Install docker-compose", fg=blue, bold=True)
            typer.echo(msg)
            server.run('sudo curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
            server.run('sudo chmod +x /usr/local/bin/docker-compose')
        except socket.error:
            typer.echo(typer.style("Unable to connect", fg=red))
            exit(0)
        except paramiko.ssh_exception.AuthenticationException:
            typer.echo(typer.style("SSH Error, verify the kay path", fg=red))
            exit(0)
