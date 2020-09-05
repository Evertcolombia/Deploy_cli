#!/usr/bin/python3
"""
Fabric script based that distributes an
archive to the web servers
"""
import socket
from datetime import datetime
from os import system
from os.path import exists, isdir

import paramiko
from typer import colors, echo, style

blue = colors.BLUE
red = colors.RED


def do_pack():
    """generates a tgz archive"""""
    try:
        #date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("landing") is False:
            system("mkdir landing")
        file_name = "landing/prototype"
        system("tar -cvzf {} landing".format(file_name))
        return file_name
    except:
        return None


def do_deploy(archive_path, server):
    """
        Distribute the files to the web server
    """
    if exists(archive_path) is False:
        return False

    try:
        filename = archive_path.split("/")[1]
        name = filename.split(".")[0]
        path = "data/landing/releases/"
        server.run('mkdir -p data/landing/releases/test data/landing/shared')
        server.run('echo "This is a test" | sudo tee data/landing/releases/test/index.html')
        server.run('sudo ln -sf data/landing/releases/test data/landing/current')
        server.put(archive_path, '/tmp/')
        server.run('mkdir -p {}{}'.format(path, name))
        server.run('tar -zxf /tmp/{} -C {}{}/'.format(filename, path, name))
        server.run('rm /tmp/{}'.format(filename))
        server.run('mv {0}{1}/landing/* {0}{1}/'.format(path, name))
        server.run('rm -rf {}{}/landing'.format(path, name))
        server.run('rm -rf data/landing/current')
        server.run('ln -s {}{}/ data/landing/current'.format(path, name))
    except socket.error:
        echo(style('unable to connect', fg=red, bold=True))
        exit(0)
    except paramiko.ssh_exception.AuthenticationException:
        echo(style("SSH Error, verify the key path", fg=red))
        exit(0)


def deploy(server):
    """Creates and distrbutes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path, server)
