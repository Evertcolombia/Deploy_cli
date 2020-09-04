#!/bin/env python3

import os
import socket

import paramiko
import typer

from .create_file import init_service_file

blue = typer.colors.BLUE
red = typer.colors.RED

def init_service(host: str, server):
    try:
        path = os.getcwd() + '/commands/modules/init_service.sh'
        init_service_file(host, path)
        server.put(path, '.')
        msg = typer.style("Update server and hostname", fg=blue, bold=True)
        typer.echo(msg)
        server.run("bash init_service.sh")
    except socket.error:
        typer.echo(typer.style('unable to connect', fg=red, bold=True))
        exit(0)
    except paramiko.ssh_exception.AuthenticationException:
        typer.echo(typer.style("SSH Error, verify the key path", fg=red))
        exit(0)
