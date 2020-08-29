#!/usr/bin/env python3

import os
import socket

import paramiko
import typer
from colored import fg, stylize

from .create_swarm_file import create_swarm_file


def init_swarm(server, hostname: str):
    try:
        path = os.getcwd() + '/commands/modules/swarm.sh'
        msg = typer.style("Init Docker Swarm Node Mannager", fg=typer.colors.BLUE, bold=True)
        typer.echo(msg)
        create_swarm_file(hostname)
        server.put(path, '/home/ubuntu')
        server.run('bash swarm.sh')
        return str(server.run('sudo docker node ls')).split()[16]
    except socket.error:
        typer.echo(typer.style("Unable to connect", fg=typer.colors.RED))
        exit(0)
    except paramiko.ssh_exception.AuthenticationException:
        typer.echo(typer.style("SSH Error, verify the kay path", fg=typer.colors.RED))
        exit(0)
