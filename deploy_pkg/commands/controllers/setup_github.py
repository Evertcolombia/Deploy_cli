#!/usr/bin/python

from os import system, getcwd, popen
from os.path import exists, isdir

from typer import colors, echo, style, prompt

def read_file(path):
    with open(path, 'r') as f:
        data = f.read().split()
    return data

def check_git(server, data):
    #conf_email = server.run('git config --get user.email')
    #conf_name = server.run('git config --get user.name')
    #print(conf_name)
    #if not conf_name:
        #print('lulu')
    server.run('git config --global user.name {}'.format(data[0]))
    #if conf_email == '':
    server.run('git config --global user.email {}'.format(data[1]))

def config_list(path, server):
    try:
        print("hereee")
        data = read_file(path)
        #check_git(server, data)
    except:
        msg = "A problem happened, make sure your git.txt file is well and try again"
        echo(style(msg, fg=colors.RED, bold=True))
        exit(0)

def setup_git(server):
    path = getcwd() + '/commands/templates/'
    filename = "git.txt"
    if exists(path + filename) is False:
        msg = "There is not a configuration file for github access. "
        msg1= "Create the a file called {} in {} with your Github username, email, url of the repository to clone and password "
        msg2 = "Ex: 'thevato admin@deploy.wtf user123 https://github.com/Evertcolombia/Deploy_cli.git' and try again."
        echo(style(msg + msg1.format(filename, path) + msg2, fg=colors.RED, bold=True))
        exit(0)
    else:
        config_list(path + filename, server)


def exec_command(branch, data, server):
    command = 'git pull origin {}'.format(branch)
    server.run(command)
    server.run(data[0])
    server.run(' '.join(data[3:]))

def make_pull(server):
        path = getcwd() + '/commands/templates/git.txt'
        if exists(path):
            data = read_file(path)
            msg = style("Enter Branch name to make pull", fg=colors.BLUE, bold=True)
            branch = prompt(msg)
            exec_command(branch, data, server)
        else:
            msg = " There is not a configuration file for github access. Create the a file called {} in {} with your Github username, email, url to the to clone repository and password Ex: 'thevato admin@deploy.wtf https://github.com/Evertcolombia/Deploy_cli.git pass123' and try again."
            echo(style(msg, fg=colors.RED, bold=True))
            exit(0)


def create_file(data):
    commands = ['#!/usr/bin/bash\n',
            'if [ ! -d "/root/viralizer" ]\nthen\n',
            "\tgit clone https://evertcolombia:'{}'@github.com/guxal/viralizer.git\n".format(' '.join(data[3:])),
            'fi']

    path = getcwd() + '/commands/templates/git_access.sh'
    with open(path, 'w') as f:
        for line in commands:
            f.write(line)
    return path

def make_clone(server):
    path = getcwd() + '/commands/templates/git.txt'
    data =  read_file(path)
    path2 = create_file(data)
    server.put(path2, '.')
    server.run('bash git_access.sh')
