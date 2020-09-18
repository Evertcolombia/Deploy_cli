#!/usr/bin/python

import os

from typer import colors, echo, style


def run_app(server, path):

    try:
        server.put(path, '.')
        echo(style("Building Application", fg=colors.BLUE, bold=True))
        server.run('bash app_file.sh')
        server.run('rm -f app_file.sh')
        os.remove(path)
    except OSError as e:
        echo(style(e, fg=colors.RED, bold=True))
        exit(0)
