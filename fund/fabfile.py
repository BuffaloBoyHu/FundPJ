# -*- coding:utf-8 -*-
import os

from fabric.api import cd, hosts, run
from fabric.operations import local
from fabric.state import env
from fabric.colors import green


@hosts('root@47.94.0.190')
def exexute_deploy():

    print green("=====================")
    code_cdir = '/root/workspace/fund-backend/FundPJ/fund'
    python_path = '/root/workspace/fundenv/bin/python'

    run('pwd')

    with cd(code_cdir):
        run('%s install -r requirements.txt' % python_path)
        run('git reset --hard')
        run('git pull origin master')

        run('%s manage.py makemigrations' % python_path)
        run('%s manage.py migrate' % python_path)
