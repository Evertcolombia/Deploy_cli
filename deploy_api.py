from os import getcwd, system
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from typer import colors, echo, style

from deploy_pkg.commands.controllers.create_connection import create_connection
from deploy_pkg.commands.controllers.create_file import app_data_file
from deploy_pkg.commands.controllers.install_docker import install_docker
from deploy_pkg.commands.controllers.install_docker_compose import \
    install_docker_compose
from deploy_pkg.commands.controllers.run_app import run_app
from deploy_pkg.commands.controllers.setup_github import make_clone, setup_git
from deploy_pkg.commands.controllers.ssh_config import init_ssh_keys


class Ssh(BaseModel):
    keyname: str
    user: str
    ip: str
    bits: Optional[int] = 2048


class Build(BaseModel):
    ip: str
    key: str
    user: str


app = FastAPI()


@app.post("/ssh-keygen")
def ssh_keygen_config(data: Ssh):
    if data.bits < 1094 and data.bits > 4096:
        data.bits = 2048
    try:
        init_ssh_keys(data.keyname, data.user, data.ip, data.bits)
        return {"Status": True, "SSH-path": "/root/{}".format(data.keyname)}
    except:
        system('rm -f $HOME/{}'.format(data.keyname))
        msg = "The Creation of keys cant' be complete now, try it again."
        msg = style(msg, fg=colors.RED, bold=True)
        return {"status": msg}


@app.post("/build")
def build_docker_and_compose(build: Build):
    try:
        server = create_connection(build.user, build.ip, build.key)
        install_docker(server)
        install_docker_compose(server)
        return {"Status": True, "docker": True, "docker-compose": True}
    except:
        return {"State": False}


@app.post("/build-app")
def build_app_on_server(service: Build):
    try:
        path = getcwd()
        if '/deploy_pkg' in path:
            path = path + '/commands/tamplates/app_file.sh'
        else:
            path = path + '/deploy_pkg/commands/templates/app_file.sh'
        server = create_connection(service.user, service.ip, service.key)
        setup_git(server)
        make_clone(server)
        app_data_file(path)
        run_app(server, path)
        return {"Status": True,
                "Path": "{}:8000/docs".format(service.ip)}
    except:
        return {"Status": False}
