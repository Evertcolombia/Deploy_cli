#!/bin/env/python3

from os import system

from typer import Argument, Typer, colors, echo, prompt, style

app = Typer()


@app.command()
def keygen(key_name: str = Argument(..., help="SSH key name"),
    user_host: str = Argument(..., help="User in the server"),
    ip: str = Argument(..., help="Server IP"),
    bit: str = Argument(..., help="bits number in the new key can be 1024 - 4096")):
    if int(bit) < 1094 and int(bit) > 4096:
        bit = '2048'
    msg = "Enter a pass phrasse for the SSH key"
    style(msg, fg=colors.BLUE, bold=True)
    phrasse = prompt(msg)

    msg = "Creating SSH keys"
    echo(style(msg, fg=colors.BLUE, bold=True))
    system('ssh-keygen -f $HOME/{} -b {} -N {}'.format(key_name, bit, phrasse))
    msg = 'Can see key file in $HOME folder '
    echo(style(msg, fg=colors.BLUE, bold=True))
    msg = "Sending key to {}".format(ip)
    echo(style(msg, fg=colors.BLUE, bold=True))
    system('ssh-copy-id -i $HOME/{} {}@{}'.format(key_name, user_host, ip))
    msg = "Send config file to ssh config in serve"
    echo(style(msg, fg=colors.BLUE, bold=True))
    system('scp -i $HOME/{} templates/ssh_config {}@{}:/etc/ssh/ssh_config'.format(key_name, user_host, ip))
