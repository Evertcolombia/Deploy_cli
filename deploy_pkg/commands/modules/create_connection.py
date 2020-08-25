#!/usr/bin/env python3

from fabric import Connection

def create_connection(user: str, ip: str, key: str):
    return Connection(host=ip,
                        user=user,
                        connect_timeout=5,
                        connect_kwargs={
                            "key_filename": key,
                        }, )
