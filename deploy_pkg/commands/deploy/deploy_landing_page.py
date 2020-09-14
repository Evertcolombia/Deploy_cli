#!/usr/bin/python3
"""
Fabric script based that distributes an
archive to the web servers
"""
import socket
from os import getcwd, path, system
from os.path import exists, isdir, isfile

import paramiko
from typer import colors, echo, style

blue = colors.BLUE
red = colors.RED


def do_pack(dir_path):
    """generates a tgz archive"""
    try:
        file_name = "{}prototype".format(dir_path)
        if isdir(dir_path) is False:
            system("mkdir {}".format(dir_path))
        if isfile(dir_path + "/docker-compose.yml") is False:
            command = 'cp {}/commands/templates/docker-compose.yml {}'
            system(command.format(getcwd(), dir_path))
        if path.isfile(dir_path + "Dockerfile") is False:
            command = 'cp {}/commands/templates/Dockerfile {}'
            system(command.format(getcwd(), dir_path))
        system("tar -cvzf {} {}".format(file_name, dir_path))
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
        name = archive_path.split("/")[-1]
        path = "data/landing/"
        server.run('mkdir -p {}'.format(path))
        server.put(archive_path, '/tmp/')
        server.run('tar -zxf /tmp/{} -C {}'.format(name, path))
        server.run('rm /tmp/{}'.format(name))
    except socket.error:
        echo(style('unable to connect', fg=red, bold=True))
        exit(0)
    except paramiko.ssh_exception.AuthenticationException:
        echo(style("SSH Error, verify the key path", fg=red))
        exit(0)


def deploy(server, dir_path):
    """Creates and distrbutes an archive to the web servers"""
    archive_path = do_pack(dir_path)
    if archive_path is None:
        return False
    return do_deploy(archive_path, server)
