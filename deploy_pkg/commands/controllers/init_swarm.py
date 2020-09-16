#!/usr/bin/env python3

import os
import socket
import sys
from commands.controllers.create_file import init_service_file, save_worker

import paramiko
from typer import colors, echo, style

blue = colors.BLUE
red = colors.RED

def init_swarm(server, hostname: str, key: str, user: str):
    try:
        path = os.getcwd() + '/commands/modules/init_service.sh'
        echo(style("Docker Swarm Node Mannager", fg=blue, bold=True))
        init_service_file(hostname, path)
        server.put(path, '.')
        server.run('bash init_service.sh')
        st = str(server.run('docker swarm init\n')).split()[28:34]
        save_worker(st, key, user)
        server.run('rm init_service.sh')

        return str(server.run('sudo docker node ls')).split()[16]
    except socket.error:
        echo(style("Unable to connect", fg=red, bold=True))
        exit(0)
    except paramiko.ssh_exception.AuthenticationException:
        echo(style("SSH Error, verify the kay path", fg=red))
        exit(0)
