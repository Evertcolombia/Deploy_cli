#!/usr/bin/python3

""" Main program side """
import typer

import commands.command_build as build

app = typer.Typer()

app.add_typer(build.app, name="build")

if __name__ == "__main__":
    app()
