#!/usr/bin/python

import os
from typing import List, Optional
from typer import Argument, Typer, colors, echo, style, Option

from commands.controllers.vultr_mannage import create_servers, destroy_servers, restart_servers, reboot_servers
from commands.controllers.vultr_functions import validate_instances

app = Typer()


@app.command()
def create(total_instances: int = Argument(..., help='specific the total of machines from 1 to 5')):
    """
        Create the number of instances that needs, min 1, max 5
    """
    total_instances = validate_instances(total_instances, "create")
    create_servers(total_instances)

@app.command()
def destroy(total_instances: int = Argument(..., help='Specific the total of machines to destroy from 1 to 5'), 
        ids: Optional[List[str]] = Option(None)):
    """
        Destroy Server Instance or instances
    """
    total_instances = validate_instances(total_instances, "destroy")
    destroy_servers(total_instances, ids)

@app.command()
def reboot(total_instances: int = Argument(..., help='Specific the total of machines to destroy from 1 to 5'),
            ids: Optional[List[str]] = Option(None)):
    """
        Reboot instances
    """
    total_instances = validate_instances(total_instances, "reboot")
    if len(ids) == 0:
        msg = "Provide server id ex:  --ids 42974163"
        echo(style(msg, fg=colors.RED, bold=True))
        exit(1)
    reboot_servers(total_instances, ids)

@app.command()
def restart(total_instances: int = Argument(..., help = 'Specific the total of machine to restart from 1 to 5'),
        ids: Optional[List[str]] = Option(None)):
    total_instances = validate_instances(total_instances, "restart")
    restart_servers(total_instances, ids)
