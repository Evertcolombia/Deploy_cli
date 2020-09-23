from os import getcwd, system
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from typer import colors, echo, style


from worker import build, ssh, build_app


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


@app.post("/ssh")
def ssh_keygen_config(data: Ssh):
    if data.bits < 1094 and data.bits > 4096:
        data.bits = 2048
    try:
        ssh.appy_async((data.keyname, data.user, data.ip, data.bits))
        return {"Status": True, "SSH-path": "/root/{}".format(data.keyname)}
    except:
        system('rm -f $HOME/{}'.format(data.keyname))
        msg = "The Creation of keys cant' be complete now, try it again."
        msg = style(msg, fg=colors.RED, bold=True)
        return {"status": msg}


@app.post("/build")
def build_docker_and_compose(builder: Build):
    try:
        build.apply_async((builder.key, builder.user, builder.ip))
        return {"Status": True, "docker": True, "docker-compose": True}
    except:
        return {"State": False}


@app.post("/build_app")
def build_app_on_server(service: Build):
    try:
        path = getcwd()
        build_app.apply_async((service.user, service.ip, service.key, path))
        return {"Status": True,
                "Path": "{}:8000/docs".format(service.ip)}
    except:
        return {"Status": False}
