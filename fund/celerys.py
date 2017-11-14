# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
from celery import Celery
import os

app = Celery('celerys')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fund.settings")

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
