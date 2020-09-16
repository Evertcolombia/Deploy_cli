#!/usr/bin/python

from os import getcwd, system

from typer import Argument, colors, echo, prompt, style


def init_ssh_keys(key, user, ip, bits):
    """
        Init the  ssh key files and configure it
        on server that user config
    """
    path = getcwd() + '/commands/templates/ssh_config'

    msg = "Creating SSH keys"
    echo(style(msg, fg=colors.BLUE, bold=True))
    system('ssh-keygen -f $HOME/{} -b {} -N ""'.format(key, bits))

    system('chmod 400 $HOME/{}'.format(key))
    msg = 'Can see key file in $HOME/{} folder'.format(key)
    echo(style(msg, fg=colors.BLUE, bold=True))

    msg = "Sending SSH key to {}".format(ip)
    echo(style(msg, fg=colors.BLUE, bold=True))
    system('chmod 700 {}'.format(path))
    system('ssh-copy-id -i $HOME/{} {}@{}'.format(key, user, ip))

    msg = "Send configuration file to HOST"
    echo(style(msg, fg=colors.BLUE, bold=True))
    command = 'scp -v -i $HOME/{} {} {}@{}:/etc/ssh/ssh_config'
    system(command.format(key, path, user, ip))
