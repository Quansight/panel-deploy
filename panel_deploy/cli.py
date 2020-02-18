import os
import tempfile

import click
from ruamel.yaml import YAML
import sys

CURRENT_DIRECTORY = os.path.normpath(os.path.abspath(os.path.dirname(__file__)))

"""
# This point of this is to give the user the following command:
'panel-deploy mynotebook.ipynb 55.23.01.123'
'panel-deploy mynotebook.ipynb 55.23.01.123 --user ubuntu '
'panel-deploy mynotebook.ipynb 55.23.01.123 --env ../../myenv.yml '
"""

@click.command()
@click.option('--environment_file_path')
@click.option('--notebook_file_path')
@click.option('--server_ip')
@click.option('--notebook_name')
@click.option('--conda_env_name')
@click.option('--server_name', default='example.com')
@click.option('--use_ssl', default=False)
@click.option('--ssl_certificate', default='')
@click.option('--ssl_certificate_key', default='')
@click.option('--current_user', default='panel')
@click.option('--secret_key', default='18233b5d-f497-48cc-9aa5-')
@click.option('--user_password', default='my4wesomep4ass')
def run(
    environment_file_path,
    notebook_file_path,
    server_ip,
    notebook_name,
    conda_env_name,
    server_name,
    use_ssl,
    ssl_certificate,
    ssl_certificate_key,
    current_user,
    secret_key,
    user_password,
):
    yaml = YAML()
    task = {}


    task["include"] = os.path.join(CURRENT_DIRECTORY, "devops", "server-setup.yml")
    task["vars"] = {
        "environment_file_path": environment_file_path,
        "notebook_file_path": notebook_file_path,
        "server_name": server_name,
        "use_ssl": use_ssl,
        "ssl_certificate": ssl_certificate,
        "ssl_certificate_key": ssl_certificate_key,
        "current_user": current_user,
        "secret_key": secret_key,
        "user_password": user_password,
        "conda_env_name": conda_env_name,
        "server_public_ip": server_ip,
        "notebook_name": notebook_name
    }

    deployment = [{"hosts": "all", "become_user": "root", "become": "yes", "tasks": [task]}]
    fp = tempfile.NamedTemporaryFile(mode="w+t", delete=True)
    fp.writelines('---\n')
    yaml.dump(deployment, fp)
    # Construct command using
    cmd = f"ansible-playbook -i {server_ip}, -u ubuntu {fp.name}"
    # Run playbook
    os.system(cmd)
    fp.close()
