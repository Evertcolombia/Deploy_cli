# Deploy_cli
------------

# Installing
------------

# Docker-Compose

```
docker-compose up -d
```

## Enter Container

```
docker-compose exec deploy bash
```


> connect your app folder with docker volumes


# USAGE
---------

## COMMANDS
- [app](#app)
- [build](#build)
- [swarm](#swarm)
- [traefik](#traefik)
- [SSH](#ssh)
- [swarmpit](#swarmpit)
- [swarmprom](#swarmprom)
- [portainer](#portainer)
- [landing](#landing)

## Use this commands for setup what you need  in a server:
----------------------------------------------------------

-[app]

This command will deploy your files to the server that you choose and run here the services that you set in your docker-compose.yml

    arguments: {
        ip: ip of the server to connect,
        key-ssh: path for the private key file,
        user-ssh: user in the server,
        dir-path: path to the app folder you will deploy
    }

    example:
        ./main.py app service 54.93.136.166 $HOME/sshkey root $HOME/app

-[build]

This command will install Docker and docker-compose in the server if they are'nt no installed yet

    arguments: {
        ip: ip of the server to connect,
        key-ssh: path for the private key file,
        user-ssh: user to use in the server
    }

    example:
        ./main.py build setup 54.93.136.166 $HOME/private ubuntu

-[landing]

This command will to deploy, setup and launch Landin web_page service in the domain that user select

     arguments: {
        ip: ip of the server to connect,
        key-ssh: path for the private key file,
        user-ssh: user to use in the server,
        host: Hostname of the server where node runs
        dir-path: path to the app folder you will deploy
    }

    example:
        ./mainy.py landing service 54.93.136.166 $HOME/sshkey ubuntu ws01.mysite.com

-[swarm]

This command will setup and launch a Docker SWARM CLOUSTER  in the server if it's not part of a clouster yet

    arguments: {
        ip: ip of the server to connect,
        key-ssh: path for the private key file,
        user-ssh: user to use in the server,
        --swarm-mode: init clouster Mannager node
    }

    example:
        ./main.py swarm clouster 54.93.136.166 $HOME/private ubuntu --swarm_mode

-[ssh]

Automated SSH keys files config in host and server

    arguments: {
        key-name: name of the new ssh keys
        user: user in the server,
        ip: ip of the server to connect,
        bit: number of bits to use when create keys
    }

    example:
        ./main.py ssh keygen newkeyName root 54.93.136.166 4096


## The follow commands will receive the same Arguments each one:
-----------------------------------------------------------------

  ### Arguments:

    arguments: {
        ip: ip of the server to connect,
        key-ssh: path for the private key file,
        user-ssh: user to use in the server,
        host: Hostname of the server where node runs
    }

-[traefik]

This command will setup and launch a load_balancer/proxy  in the domain that user puts

    example:
        ./mainy.py traefik service 54.93.136.166 $HOME/sshkey ubuntu ws01.mysite.com

-[swarmpit]

This command will setup and launch a Swarmpit service in the domain that user puts

    example:
        ./mainy.py swarmpit service 54.93.136.166 $HOME/sshkey ubuntu ws01.mysite.com

-[swarmprom]

This command will setup and launch Swarmprom service in the domain that user puts

    example:
        ./mainy.py traefik service 54.93.136.166 $HOME/sshkey ubuntu ws01.mysite.com


-[portainer]

This command will setup and launch Portainer service in the domain that user puts

    example:
        ./mainy.py portainer service 54.93.136.166 $HOME/sshkey ubuntu ws01.mysite.com


# AUTHORS
* **Guxal** ([@guxal](https://github.com/guxal))
* **Evert Escalante** ([@evertcolombia](https://github.com/evertcolombia))


# License
## MIT Free Software, Hell Yeah!
