#!/usr/bin/python3

""" Main program side """
import commands.command_build as build
import commands.command_traefik_service as traefik_service
import commands.command_docker_swarm as init_swarm
import typer

app = typer.Typer()

app.add_typer(build.app, name="build")
app.add_typer(traefik_service.app, name="init-traefik")
app.add_typer(init_swarm.app, name="init-swarm")

if __name__ == "__main__":
    app()
