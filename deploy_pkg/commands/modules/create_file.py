#!/bin/env python3

import os

import typer

blue = typer.colors.BLUE

def init_service_file(hostname, path):
    data = ['#!/usr/bin/bash\n',
            'export USE_HOSTNAME={}\n'.format(hostname),
            'echo $USE_HOSTNAME > /etc/hostname\n',
            'sudo hostname -F /etc/hostname\n',
            'sudo apt-get update\n',
            'sudo apt-get upgrade -y']
    create_file(data, path)


def traefik_data_file(path: str):
    msg = "You need a subdomain for Traefik dashboard Make you sure that subdomain points to a valid IP and is set in the hosting service as something like this: traefik.sys.mysite.com\n Enter subdomain name"
    msg = typer.style(msg, fg=blue, bold=True)
    domain = typer.prompt(msg)
    username = typer.prompt('Enter username')
    email = typer.prompt('Enter email')
    password = typer.prompt('Enter password', confirmation_prompt=True, hide_input=True)
    data = ['#!/usr/bin/bash\n',
            'sudo chmod 666 /var/run/docker.sock\n',
            'docker network create --driver=overlay traefik-public\n',
            "export NODE_ID=$(docker info -f '{{.Swarm.NodeID}}')\n",
            'sudo docker node update --label-add traefik-public.traefik-public-certificates=true $NODE_ID\n',
            'export EMAIL={}\n'.format(email),
            'export DOMAIN={}\n'.format(domain),
            'export USERNAME={}\n'.format(username),
            'export PASSWORD={}\n'.format(password),
            'export HASHED_PASSWORD=$(openssl passwd -apr1 $PASSWORD)\n',
            'curl -L dockerswarm.rocks/traefik.yml -o traefik.yml\n',
            'docker stack deploy -c traefik.yml traefik\n',
            'docker stack ls\n',
            'docker stack ps traefik\n']
    create_file(data, path)
    return domain

def create_file(data, path):
    with open(path, 'w') as f:
        for line in data:
            f.write(line)
