from celery import Celery
from celery.utils.log import get_task_logger
from deploy_pkg.commands.controllers.ssh_config import init_ssh_keys
from deploy_pkg.commands.controllers.create_connection import create_connection
from deploy_pkg.commands.controllers.install_docker import install_docker
from deploy_pkg.commands.controllers.install_docker_compose import \
   install_docker_compose
from deploy_pkg.commands.controllers.setup_github import make_clone, setup_git
from deploy_pkg.commands.controllers.create_file import app_data_file
from deploy_pkg.commands.controllers.run_app import run_app
# Create the Celery app and get the  logger
celery_app = Celery('tasks',
broker='pyamqp://guest@rabbit//')
logger = get_task_logger(__name__)


@celery_app.task
def ssh(key, user, ip, bits):
    init_ssh_keys(key, user, ip, bits)


@celery_app.task
def build(key, user, ip):
    try:
        server = create_connection(user, ip, key)
        install_docker(server)
        install_docker_compose(server)
    except:
        return False


@celery_app.task
def build_app(user, ip, key, path):
    try:
        server = create_connection(user, ip, key)
        setup_git(server)
        path = path + '/deploy_pkg/commands/templates/app_file.sh'
        make_clone(server)
        logger.info(path)
        app_data_file(path)
        run_app(server, path)
    except:
        return False
