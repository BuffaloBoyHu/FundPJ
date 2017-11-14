# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
from celery import Celery
import os

# 获取当前文件夹名，即为该Django项目的项目名
project_name = os.path.split(os.path.abspath('.'))[-1]

app = Celery(project_name)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
