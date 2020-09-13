#!/usr/bin/python3

""" Main program side """
import commands.command_build as build
import commands.command_docker_swarm as init_swarm
import commands.command_landing_service as landing_service
import commands.command_portainer_service as portainer_service
import commands.command_ssh_key_connect as init_ssh
import commands.command_swarmpit_service as swarmpit_service
import commands.command_swarmprom_service as swarmprom_service
import commands.command_traefik_service as traefik_service
import commands.command_app_service as app_service
import typer

app = typer.Typer()

app.add_typer(init_ssh.app, name="ssh")
app.add_typer(build.app, name="build")
app.add_typer(traefik_service.app, name="traefik")
app.add_typer(init_swarm.app, name="swarm")
app.add_typer(portainer_service.app, name="portainer")
app.add_typer(swarmprom_service.app, name='swarmprom')
app.add_typer(swarmpit_service.app, name='swarmpit')
app.add_typer(landing_service.app, name='landing')
app.add_typer(app_service.app, name='app')


if __name__ == "__main__":
    app()
