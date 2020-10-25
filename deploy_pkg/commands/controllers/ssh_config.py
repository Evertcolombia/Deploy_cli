#!/usr/bin/python

from os import getcwd, system

from typer import Argument, colors, echo, prompt, style


def init_ssh_keys(key, user, ip, bits):
    """
        Init the  ssh key files and configure it
        on server that user config
    """
    path = getcwd()
    if '/deploy_pkg' in path:
        path = path + '/commands/templates/ssh_config'
    else:
        path = path + '/deploy_pkg/commands/templates/ssh_config'

    print("HEREEEEE")
    print("PATH")
    print(path)

    msg = "Creating SSH keys"
    echo(style(msg, fg=colors.BLUE, bold=True))
    system('ssh-keygen -f ~/.ssh/{} -b {} -N ""'.format(key, bits))

    system('chmod 400 ~/.ssh/{}'.format(key))
    msg = 'Can see key file in ~/.ssh/{} folder'.format(key)
    echo(style(msg, fg=colors.BLUE, bold=True))



    try:
        msg = "Sending SSH key to {}".format(ip)
        echo(style(msg, fg=colors.BLUE, bold=True))
        system('chmod 700 {}'.format(path))
        system('sshpass -f password.txt ssh-copy-id -i ~/.ssh/{} {}@{}'.format(key, user, ip))
    except:
        msg = "There is not a password.txt file with the server password at /code "
        echo(style("{} Create the file and try again".format(msg), fg=colors.BLUE))
        exit(0)

    msg = "Send configuration file to HOST"
    echo(style(msg, fg=colors.BLUE, bold=True))
    command = 'scp -v -i ~/.ssh/{} {} {}@{}:/etc/ssh/ssh_config'
    system(command.format(key, path, user, ip))
