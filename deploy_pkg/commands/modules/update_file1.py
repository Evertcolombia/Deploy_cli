#!/usr/bin/env python3

import os


def update_init_service_file(hostname):

    path = os.getcwd() + '/commands/modules/text1.sh'
    data = ['#!/usr/bin/bash\n',
            'export USE_HOSTNAME={}\n'.format(hostname),
            'echo $USE_HOSTNAME > /etc/hostname\n',
            'sudo hostname -F /etc/hostname\n',
            'sudo apt-get update\n',
            'sudo apt-get upgrade -y\n']
    with open(path, 'w') as f:
        for line in data:
            f.write(line)
