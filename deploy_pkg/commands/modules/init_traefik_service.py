#!/usr/bin/ennv python3

import os
import socket
from commands.modules.update_File2 import create_traefik_sh_file

import paramiko
import typer

color = typer.colors


def init_traefik_service(server,
                         username: str,
                         password: str,
                         email: str,
                         domain: str):
    """This function creates a Traefik main load
        balancer/proxy server to handle connections
    """
    try:
        path = os.getcwd() + '/commands/modules/text2.sh'
        msg = typer.style('Creating a network between Traefik and the containers')
        typer.echo(msg)
        print(username + ' ' + domain + ' ' + password + ' ' + email)
        create_traefik_sh_file(email, password, domain, username)
        server.put(path, '/home/ubuntu')
        server.run("bash text2.sh")
    except socket.error:
        typer.echo(typer.style('unable to connect', fg=color.RED, bold=True))
        exit(0)
    except paramiko.ssh_exception.AuthenticationException:
        typer.echo(typer.style("SSH Error, verify the key path", fg=color.RED, bold=True))
        exit(0)
