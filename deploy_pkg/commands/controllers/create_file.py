#!/bin/env python3

import os

from typer import colors, echo, prompt, style

blue = colors.BLUE

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
    style(msg, fg=blue, bold=True)
    domain = prompt(msg)
    username = prompt('Enter username')
    email = prompt('Enter email')
    password = prompt('Enter password', confirmation_prompt=True, hide_input=True)
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

def portainer_data_file(path: str):
    msg = "You need a subdomain for Portainer UX Make you sure that subdomain points to a valid IP and this set in the hosting service as something like this: portainer.sys.mysite.com\n Enter subdomain name"
    style(msg, fg=blue, bold=True)
    domain = prompt(msg)
    data = ['#!/usr/bin/bash\n',
            'export DOMAIN={}\n'.format(domain),
            "export NODE_ID=$(docker info -f '{{.Swarm.NodeID}}')\n",
            'docker node update --label-add portainer.portainer-data=true $NODE_ID\n',
            'curl -L dockerswarm.rocks/portainer.yml -o portainer.yml\n',
            'docker stack deploy -c portainer.yml portainer']
    create_file(data, path)
    return domain

def swarmprom_data_file(path: str):

    username = prompt(style('Enter Username', fg=blue, bold=True))
    msg = style('Enter Password', fg=blue, bold=True)
    admin_pass = prompt(msg, confirmation_prompt=True, hide_input=True)
    msg = "You need a list of subdomain pointing to your server/s for the diffrents services that Swamprom provides. Make you sure that subdomain's points to a valid IP and this set in the hosting service\n Please the the follow subdomain's in your hosting: [grafana.mysite.com, alertmanager.mysite.com, unsee.mysite.com, prometheus.mysite.com]"
    echo(style(msg, fg=blue, bold=True))
    msg = "Enter domain for the service ex('mysite.com')"
    domain = prompt(style(msg, fg=blue, bold=True))
    data = ['#!/usr/bin/bash\n',
            'cd swarmprom\n'
            'export ADMIN_USER={}\n'.format(username),
            'export ADMIN_PASSWORD={}\n'.format(admin_pass),
            'export HASHED_PASSWORD=$(openssl passwd -apr1 $ADMIN_PASSWORD)\n',
            'export DOMAIN={}\n'.format(domain),
            'curl -L dockerswarm.rocks/swarmprom.yml -o swarmprom.yml\n',
            'docker stack deploy -c swarmprom.yml swarmprom']

    create_file(data, path)
    return domain

def swarmpit_data_file(path: str):
    msg = "You need a subdomain for swarmpit UX Make you sure that subdomain points to a valid IP and set in the hosting service like this: swamrpit.mysite.com\n Enter subdomain name"
    style(msg, fg=blue, bold=True)
    domain = prompt(msg)
    data = ['#!/usr/bin/bash\n',
            'export DOMAIN={}\n'.format(domain),
            "export NODE_ID=$(docker info -f '{{.Swarm.NodeID}}')",
            'docker node update --label-add swarmpit.db-data=true $NODE_ID\n',
            'docker node update --label-add swarmpit.influx-data=true $NODE_ID\n',
            'curl -L dockerswarm.rocks/swarmpit.yml -o swarmpit.yml\n',
            'docker stack deploy -c swarmpit.yml swarmpit\n',
            'docker stack ps swarmpit\n',
            'docker service logs swarmpit_app']
    create_file(data, path)
    return domain


def landing_data_file(path:str, dir_path: str):
    msg = "You need a subdomain for Landing service, make you sure that subdomain points to a valid IP ex('landing.mysite.com')\n Enter subdomain name"
    msg = style(msg, fg=blue, bold=True)
    domain = prompt(msg)
    dir_path = dir_path.split("/")[-2]
    data = ['#!/usr/bin/bash\n',
            'export DOMAIN={}\n'.format(domain),
            "export NODE_ID=$(docker info -f '{{.Swarm.NodeID}}')\n",
            'docker node update --label-add landing.landing-data=true $NODE_ID\n',
            'mv data/landing/home/fantasma/* data/\n',
            'rm -rf data/landing\n',
            'docker stack deploy -c data/{}/docker-compose.yml landing\n'.format(dir_path),
            'docker stack ls\n',
            'docker stack ps landing']
    create_file(data, path)
    return domain

def app_data_file(pathstr):
    data = ['#!/usr/bin/bash\n',
            'cd viralizer/\n',
            'docker-compose up -d']
    create_file(data, path)


def create_file(data, path):
    with open(path, 'w') as f:
        for line in data:
            f.write(line)
