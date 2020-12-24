from vultr import Vultr, VultrError

from json import dumps, load
from typer import echo, colors, style

apiKey = "QFPLG3E63OARYJY3PNXLETKKPO5PGI7TWWEA"
vultr = Vultr(apiKey)


def get_server_list():
    try:
        server_list = vultr.server.list()
        response = {}

        for key, value in server_list.items():
            res = {}
            res["ip"] = value["main_ip"]
            res["location"] = value["location"]
            res["password"] = value["default_password"]
            res["status"] = value["status"]
            res["date_created"] = value["date_created"]
            response[key] = res
    
        return response
    except VultrError as ex:
        print(ex)
        exit(1)

def get_region_list():
    try:
        regions_list = vultr.regions.list()
        response = {}

        for key, value in regions_list.items():
            res = {}
            res["city_name"] = value["name"]
            res["country"] = value["country"]
            res["continent"] = value["continent"]
            response[key] = res
        
        return response
    except VultrError as ex:
        print(ex)
        exit(1) 

def get_plans_list():
    try:
        plans_list = vultr.plans.list()
        response = {}
        count = 0
    
        for key, value in plans_list.items():
            if (count < 1):
                res = {}
                res["price_per_month"] = value["price_per_month"]
                res["available_locations"] = value["available_locations"]
                res["features"] = value["name"]
                response[key] = res
            count = count + 1

        return response
    except VultrError as ex:
        print(ex)
        exit(1)


def get_iso_list():
    try:
        os_list = vultr.os.list()
        response = {}

        for key, value in os_list.items():
            res = {}
            res["ISOID"] = value["OSID"]
            res["name"] = value["name"]
            response[key] = res
        print(len(response))
        return response

    except VultrError as ex:
        print(ex)
        exit(1)

def get_available_locations():
    try:
        plan_list = get_plans_list()
        locations = []
        regions = get_region_list()
        
        for key, value in regions.items():
            if int(key) in plan_list["201"]["available_locations"]:
                reg = {}
                reg["id"] = key
                reg["name"] = value["city_name"]
                locations.append(reg)
        return locations
        #server  = vultr.server.create(2, 201, 270)

    except VultrError as ex:
        print(ex)
        exit(1)

def launch_server(city_id):
    try:
        res = vultr.server.create(city_id, 201, 270)
        return res
    except VultrError as ex:
        print(ex)
        exit(1)


def validate_instances(quantity, case):
    if quantity > 5:
        msg = "total_instances is bigger than max (5), it will to {} the total available instances \
                for this Vultr Account"
        if case == "create":
            echo(style(msg.format("CREATE"), fg=colors.GREEN, bold=True))
        elif case == "destroy":
            echo(style(msg.format("DESTROY"), fg=colors.RED, bold=True))
        elif case == "reboot":
            echo(style(msg.format("REBOOT"), fg=colors.GREEN, bold=True))
        aquantity = 5
    elif quantity < 1:
        msg = "total_instances is less than 1 it will to {} one machine"
        if case == "create":
            echo(style(msg.format("CREATE"), fg=colors.GREEN, bold=True))
        elif case == "destroy":
            echo(style(msg.format("DESTROY"), fg=colors.RED, bold=True))
        elif case == "reboot":
            echo(style(msg.format("REBOOT"), fg=colors.GREEN, bold=True))
        quantity = 1
    elif type(quantity) != int:
        msg = 'total_instances must be a number'
        echo(style(fg=colors.RED, bold=True))
        exit(1)
    return quantity

def delete_instance(subid):
    try:
        msg = "Deleting instance: {}".format(subid)
        echo(style(msg, fg=colors.GREEN, bold=True))
        response = vultr.server.destroy(subid)
    except VultrError as ex:
        print(ex)
        exit(1)

def reboot_instance(subid):
    try:
        msg = "Reboot instance: {}".format(subid)
        echo(style(msg, fg=colors.GREEN, bold=True))
        response = vultr.server.reboot(subid)
    except VultrError as ex:
        print(ex)
        exit(1)

def restart_instance(subid):
    try:
        msg = "Restarting instance: {}".format(subid)
        echo(style(msg, fg=colors.RED, bold=True))
        response = vultr.server.start(subid)
    except VultrError as ex:
        print(ex)
        exit(1)
