# -*- coding: utf-8 -*-
from celery import app
import time


@app.task
def sendmail():
    print" ==== start send email ======"
    time.sleep(5)
    print "======= end send ========="
