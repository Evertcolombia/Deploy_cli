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
---------

## COMMANDS
- [build](#build)
- [swarm](#swarm)
- [traefik](#traefik)
- [swarmpit](#swarmpit)
- [swarmprom](#swarmprom)
- [portainer](#portainer)
- [landing](#landing)

Use this commands for setup  each service in a server:

-[build]

This command will install Docker and docker-compose in the server if they are'nt no installed yet

arguments: {
    ip: ip of the server to connect,
    key-ssh: path for the private key file,
    user-ssh: user to use in the server,
    host: Hostname of the server where node runs
}

    python3 mainy.py build setup 54.93.136.166 $HOME/private.pem ubuntu ws01.mysite.com

-[swarm]

This command will setup and launch a Docker SWARM CLOUSTER  in the server if it's not part of a clouster yet

arguments: {
    ip: ip of the server to connect,
    key-ssh: path for the private key file,
    user-ssh: user to use in the server,
    --swarm-mode: init clouster
}

    python3 main.py swarm clouster 54.93.136.166 $HOME/private.pem ubuntu --swarm_mode

-[traefik]

This command will setup and launch a load_balancer/proxy  in the domain that user puts

arguments: {
    ip: ip of the server to connect,
    key-ssh: path for the private key file,
    user-ssh: user to use in the server,
    host: Hostname of the server where node runs
}

    python3 mainy.py traefik service 54.93.136.166 $HOME/private.pem ubuntu ws01.mysite.com

-[swarmpit]

This command will setup and launch a Swarmpit service in the domain that user puts

arguments: {
    ip: ip of the server to connect,
    key-ssh: path for the private key file,
    user-ssh: user to use in the server,
    host: Hostname of the server where node runs
}

    python3 mainy.py swarmpit service 54.93.136.166 $HOME/private.pem ubuntu ws01.mysite.com

-[swarmprom]

This command will setup and launch Swarmprom service in the domain that user puts

arguments: {
    ip: ip of the server to connect,
    key-ssh: path for the private key file,
    user-ssh: user to use in the server,
    host: Hostname of the server where node runs
}

    python3 mainy.py traefik service 54.93.136.166 $HOME/private.pem ubuntu ws01.mysite.com
    

-[portainer]

This command will setup and launch Portainer service in the domain that user puts

arguments: {
    ip: ip of the server to connect,
    key-ssh: path for the private key file,
    user-ssh: user to use in the server,
    host: Hostname of the server where node runs
}

    python3 mainy.py portainer service 54.93.136.166 $HOME/private.pem ubuntu ws01.mysite.com
    

-[landing]

This command will setup and launch Landin web_page service in the domain that user puts

arguments: {
    ip: ip of the server to connect,
    key-ssh: path for the private key file,
    user-ssh: user to use in the server,
    host: Hostname of the server where node runs
}

    python3 mainy.py landing service 54.93.136.166 $HOME/private.pem ubuntu ws01.mysite.com


# AUTHORS
* **Guxal** ([@guxal](https://github.com/guxal))
* **Evert Escalante** ([@evertcolombia](https://github.com/evertcolombia))


# License
## MIT Free Software, Hell Yeah!
