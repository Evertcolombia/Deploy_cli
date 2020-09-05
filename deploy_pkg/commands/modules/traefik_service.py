#!/bin/env python3

import os
import socket
from commands.controllers.create_file import traefik_data_file

import paramiko
from typer import colors, echo, style

blue = colors.BLUE
red = colors.RED


def init_traefik_service(server):
    """Setup a main load balancer/proxy server
       to handle connections
    """
    try:
        path = os.getcwd() + '/commands/templates/traefik_file.sh'
        echo(style('Networ between Traefik and containers', fg=blue))
        domain = traefik_data_file(path)
        server.put(path, '.')
        server.run("bash traefik_file.sh")
        server.run("rm traefik_file.sh")
        #os.remove(path)
        return domain
    except socket.error:
        echo(style('unable to connect', fg=red, bold=True))
        exit(0)
    except paramiko.ssh_exception.AuthenticationException:
        echo(style("SSH Error, verify the key path", fg=red))
        exit(0)
