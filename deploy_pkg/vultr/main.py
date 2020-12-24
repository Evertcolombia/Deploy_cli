#!/usr/bin/python

""" Main program side """
import commands.command_vultr_create as servers_create
import typer


app = typer.Typer()
app.add_typer(servers_create.app, name='vultr')

if __name__ == "__main__":
    app()
