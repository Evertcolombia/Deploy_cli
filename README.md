# Deploy_cli
------------

# Installing
------------

You sould have ```Python3.6``` or higher

Install and update using pip
```
pip install -r requirements.txt
```

# USAGE
--------

Use this command for setup server with initial packages
arguments are represented by -- example: --ip

arguments: {
    --ip: ip of the server to connect,
    --key-ssh: path for the private key file,
    --user-ssh: user to use in the server,
    --swarm-mode: [optional]
}

    python3 main.py build setup --ip ssh-key ssh-user
    ==
    python3 mainy.py build setup 54.93.136.166 $HOME/private.pem ubuntu


If want to init Docker Swarm Mode in this server user --swarm-mode flag

    python3 main.py build setup 54.93.136.166 $HOME/private.pem ubuntu --swarm_mode

it will create a Mannager node from this server

* This install [Docker, docker-compose, Swarm mode(optional)]

# AUTHORS
## - Guxal  | https://github.com/guxal/
## - Evertcolombia | https://github.com/evertcolombia/

# License
## MIT Free Software, Hell Yeah!