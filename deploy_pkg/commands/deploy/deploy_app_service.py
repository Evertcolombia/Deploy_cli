#!/usr/bin/python

import socket
from os import system
from os.path import exists, isdir

import paramiko
from typer import colors, echo, style


def do_pack(dir_path):
    try:
        if isdir(dir_path) is False:
            echo(style("Folder Don't exists", fg=colors.RED, bold=True),)
            exit(0)
        file_name = dir_path + "prototype"
        system("sudo tar -cvzf {} {}".format(file_name, dir_path))
        return file_name
    except:
        return None

def do_deploy(archive_path, server):
    if exists(archive_path) is False:
        return False

    try:
        folder = archive_path.split("/")[3]
        file_name = archive_path.split("/")[-1]
        server.run('mkdir -p {}'.format(folder))
        server.put(archive_path, '/tmp/')
        server.run('tar -zxf /tmp/{} -C .'.format(file_name))
        server.run('cp -r home/fantasma/viralizer/* viralizer/')
        server.run('rm -rf home/')
        server.run('rm /tmp/{}'.format(file_name))
    except socket.error:
        echo(style('unable to connect', fg=colors.RED, bold=True))
        exit(0)
    except paramiko.ssh_exception.AuthenticationException:
        echo(style("SSH Error, verify the key path", fg=colors.RED, bold=True))
        exit(0)

def deploy(server, dir_path):
    archive_path = do_pack(dir_path)
    if archive_path is None:
        return False
    return do_deploy(archive_path, server)
