#!/bin/env python3

import os


def create_swarm_file(hostname):
    path = os.getcwd() + '/commands/modules/swarm.sh'
    data = ['#!/usr/bin/bash\n',
            'export USE_HOSTNAME={}\n'.format(hostname),
            'echo $USE_HOSTNAME > /etc/hostname\n',
            'sudo hostname -F /etc/hostname\n',
            'sudo apt-get update\n',
            'sudo apt-get upgrade -y\n',
            'sudo docker swarm init',
            ]
    with open(path, 'w') as f:
        for line in data:
            f.write(line)
