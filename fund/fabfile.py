# -*- coding:utf-8 -*-
import os

from fabric.api import cd, hosts, run
from fabric.operations import local
from fabric.state import env


@hosts('47.94.0.190')
def exexute_deploy():
    if env.ssh_config_path and os.path.isfile(os.path.expanduser(env.ssh_config_path)):
        env.use_ssh_config = True
    else:
        env.user = 'root'
        env.password = '8756117hu'

    code_cdir = '/root/workspace/fund-backend/FundPJ/fund'
    python_path = '/root/workspace/fundenv/bin/python'

    with cd(code_cdir):
        # run('git reset --hard')
        run('git pull origin master')

        run('%s manage.py makemigrations' % python_path)
        run('%s manage.py migrate' % python_path)
