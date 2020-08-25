#!/usr/bin/env python3

import socket

import paramiko
import typer
from colored import fg, stylize


def install_docker_compose(server):
    try:
        server.run('docker-compose -v')
    except:
        try:
            msg = typer.style("Install current stable release of docker-compose", fg=typer.colors.BLUE, bold=True)
            typer.echo(msg)
            server.run('sudo curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
            server.run('sudo chmod +x /usr/local/bin/docker-compose')
        except socket.error:
            typer.echo(stylize(f"Unable to connect", fg("red")))
            exit(0)
        except paramiko.ssh_exception.AuthenticationException:
            typer.echo(stylize(f"SSH Error, verify the kay path", fg("red")))
            exit(0)
