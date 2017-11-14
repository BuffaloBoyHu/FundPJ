# -*- coding:utf-8 -*-
import os

from fabric.api import cd, hosts, run
from fabric.operations import local
from fabric.state import env
from fabric.colors import green


@hosts('root@47.94.0.190')
def excute_deploy():
    print green("=====================")
    code_cdir = '/root/workspace/fund-backend/FundPJ/fund'
    python_path = '/root/workspace/fundenv/bin/python'
    pip_path = '/root/workspace/fundenv/bin/pip'

    with cd(code_cdir):
        run('rm *.pyc')  # 删除已经生成的编译文件
        run('%s install -r requirements.txt' % pip_path)
        run('git reset --hard')
        run('git pull origin master')

        run('%s manage.py makemigrations' % python_path)
        run('%s manage.py migrate' % python_path)
