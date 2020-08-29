#!/usr/bin/env python3

import os


def create_traefik_sh_file(email: str,
                           password: str,
                           domain: str,
                           username: str,
):

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
    path = os.getcwd() + '/commands/modules/text2.sh'
    print(email + password + domain + username)

    with open(path, 'w') as f:
        for line in data:
            f.write(line)
            print(line)
