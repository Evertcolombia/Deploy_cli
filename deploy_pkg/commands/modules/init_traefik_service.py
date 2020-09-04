#!/usr/bin/ennv python3

import os
import socket
from commands.modules.create_file import traefik_data_file

import paramiko
import typer

blue = typer.colors.BLUE
red = typer.colors.RED


def init_traefik_service(server):
    """Setup a main load balancer/proxy server
       to handle connections
    """
    try:
        path = os.getcwd() + '/commands/modules/traefik_file.sh'
        msg = typer.style('Networ between Traefik and containers', fg=blue)
        typer.echo(msg)
        domain = traefik_data_file(path)
        server.put(path, '.')
        server.run("bash traefik_file.sh")
        server.run("rm traefik_file.sh")
        return domain
    except socket.error:
        typer.echo(typer.style('unable to connect', fg=red, bold=True))
        exit(0)
    except paramiko.ssh_exception.AuthenticationException:
        typer.echo(typer.style("SSH Error, verify the key path", fg=red))
        exit(0)
