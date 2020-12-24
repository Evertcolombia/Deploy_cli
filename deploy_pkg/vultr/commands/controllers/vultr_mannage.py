#!/usr/bin/python

from typer import colors, echo, style, prompt
from commands.controllers.vultr_functions import get_available_locations, get_server_list, launch_server, delete_instance, reboot_instance, restart_instance


def create_servers(total_instances):

    try:
        server_count = len(get_server_list())
        if (server_count >= 5):
            msg = "This account have 5 intances running, Destroy at least one \
                    before to try again."
            echo(style(msg, fg=colors.RED, bold=True))
            exit(1)
        
        st = []
        server_count = 5 - server_count

        if server_count >  1:
            locations = get_available_locations()
            for lc in locations:
                st.append("{} : {}\n".format(lc["id"], lc["name"]))
       
            msg = "This account cant only create {} instances, please insert the id for the \
                     cities that will be launch separed by spaces: \n".format(server_count)
            echo(style(msg, fg=colors.GREEN, bold=True))       
            cities = prompt(''.join(st))
            cities = cities.split()

            if total_instances > server_count:
                total_instances = server_count

            for el in range(total_instances):
                res = launch_server(int(cities[el]))
                print(res)
    except:
        pass
    
def destroy_servers(total_instances, server_ids):

    try:
        server_list = get_server_list()
        
        if len(server_list) < 1:
            echo(style("there are not servers to destroy", fg=colors.RED, bold=True))
            exit(1)

        if total_instances > len(server_list):
            total_instances -= len(server_list)
        
        if total_instances == 1 and server_ids[0] in server_list.keys():
            delete_instance(server_ids[0])

        if total_instances > 1:
            count = 0
            for id in server_ids:
                if id in server_list.keys() and count < total_instances:
                    delete_instance(id)
                count += 1
    except:
        pass

def reboot_servers(total_instances, server_ids):
    try:
        server_list = get_server_list()
        server_len = len(server_list)
       
        if server_len < 1:
            echo(style("No servers to reboot", fg=colors.RED, bold=True))
            exit(1)

        if total_instances > server_len:
            total_instances -= server_len
        
        if total_instances == 1 and server_ids[0] in server_list.keys():
            reboot_instance(server_ids[0])

        if total_instances > 1:
            count = 0
            for id in server_ids:
                if id in server_list.keys() and count < total_instances:
                    reboot_instance(id)
                count += 1
    except:
        pass

def restart_servers(total_instances, ids):
    try:
        server_list = get_server_list()
        server_len = len(server_list)

        if server_len < 1:
            echo(style("No servers to Restart", fg=colors.RED, bold=True))
            exit(1)
        if total_instances > server_len:
            total_instances -= server_len
        
        if total_instances == 1 and ids[0] in server_list.keys():
            restart_instance(ids[0])

        if total_instances > 1:
            count = 0
            print(ids)
            print(server_list)
            for id in server_list.keys():
                if  id in ids and count < total_instances:
                    restart_instance(id)
                    count += 1
    except:
        pass
