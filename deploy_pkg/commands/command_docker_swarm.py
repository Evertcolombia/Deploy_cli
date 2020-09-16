#!/usr/bin/python3

import os
from commands.controllers.create_connection import create_connection
from commands.controllers.init_service import init_service
from commands.controllers.init_swarm import init_swarm
from commands.controllers.install_docker import install_docker
from commands.controllers.install_docker_compose import install_docker_compose
from typing import Optional

from typer import Argument, Typer, colors, echo, prompt, style

app = Typer()
blue = colors.BLUE
red = colors.RED


@app.command()
def init_cluster(ip: str = Argument(..., help="Server IP"),
        key_ssh: str = Argument(..., help="Path to ssh key file"),
        user_ssh: str = Argument(..., help="User to use in serve"),
        hostname: str = Argument(..., help="Ex: ws01.example.com"),
        swarm_mode: Optional[bool] = False
):
    """Init Swarm Mode"""
    if swarm_mode:
        server = create_connection(user_ssh, ip, key_ssh)
        n_tkn = init_swarm(server, hostname, key_ssh, user_ssh)
        echo(style("Manager Node Token: {}".format(n_tkn), fg=blue, bold=True))
    else:
        echo(style("--swarm-mode must be set", fg=red, bold=True))
        exit(0)

@app.command()
def add_worker(ip: str = Argument(..., help="Server IP"),
        key_ssh: str= Argument(..., help="Path to ssh key file"),
        user_ssh: str = Argument(..., help="User in the server"),
        hostname: str = Argument(..., help="Ex: ws01.example.com"),
        mannager_ip: str = Argument(..., help="Mannager cluster IP")):
    """Add Worker to Manager Node"""
    registers = os.getcwd() + '/commands/templates/manager_registers.txt'
    if os.path.exists(registers):
        with open(registers, 'r') as f:
            line = f.readline()
            while line:
                line = line.split(' ')
                line_ip = line[-3].split(':')[0]
                if line_ip == mannager_ip:
                    echo(style("Connecting with Server", fg=blue, bold=True))
                    server = create_connection(user_ssh, ip, key_ssh)
                    install_docker(server)
                    install_docker_compose(server)
                    init_service(hostname, server)
                    server.run(' '.join(line[:-2]))
                    break
                else:
                    line = f.readline()

        msg = 'Not registers for the mannager server ip'
        echo(style(msg, fg=blue, bold=True))
        msg = 'Enter server user for of mannager node'
        user = prompt(style(msg, fg=blue, bold=True))
        msg = style('Enter path to ssh key file', fg=blue, bold=True)

        msg = style('Enter path to ssh key file', fg=blue, bold=True)
        key = prompt(msg)
        server = create_connection(user, mannager_ip, key)
        st = str(server.run('docker swarm join-token worker')).split()
        print(st)
    else:
        msg = 'Not registers for the mannager server ip'
        echo(style(msg, fg=blue, bold=True))

        msg = 'Enter server user for of mannager node'
        user = prompt(style(msg, fg=blue, bold=True))
        msg = style('Enter path to ssh key file', fg=blue, bold=True)
        key = prompt(msg)
        #server = create_connection(user, ip_mannager, key)
