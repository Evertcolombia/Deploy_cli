#!/usr/bin/env python3

import socket

import paramiko
import typer
from colored import fg, stylize


def init_swarm(server):
    try:
        server.run('sudo apt-get update')
        server.run('sudo apt-get upgrade -y')
        typer.echo("Init Docker Swarm Node Manager")
        #server.run('sudo docker swarm leave --force')
        server.run('sudo docker swarm init')
        return str(server.run('sudo docker node ls')).split()[16]
    except socket.error:
        typer.echo(stylize(f"Unable to connect", fg("red")))
        exit(0)
    except paramiko.ssh_exception.AuthenticationException:
        typer.echo(stylize(f"SSH Error, verify the kay path", fg("red")))
        exit(0)
