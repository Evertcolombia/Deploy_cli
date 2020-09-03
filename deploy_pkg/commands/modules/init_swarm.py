#!/usr/bin/env python3

import os
import socket
import sys

import paramiko
import typer

from .create_file import init_service_file

blue = typer.colors.BLUE
red = typer.colors.RED

def init_swarm(server, hostname: str):
    try:
        path = os.getcwd() + '/commands/modules/init_service.sh'
        msg = typer.style("Docker Swarm Node Mannager", fg=blue, bold=True)
        typer.echo(msg)
        init_service_file(hostname, path)
        server.put(path, '.')
        server.run('bash init_service.sh')
        server.run('docker swarm init\n')
        server.run('rm init_service.sh')
        return str(server.run('sudo docker node ls')).split()[16]
    except socket.error:
        typer.echo(typer.style("Unable to connect", fg=red, bold=True))
        sys.exit(0)
    except paramiko.ssh_exception.AuthenticationException:
        typer.echo(typer.style("SSH Error, verify the kay path", fg=red))
        sys.exit(0)
