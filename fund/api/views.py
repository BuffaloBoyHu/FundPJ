# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from spider.tasks import sendmail
from celerys import debug_task


# Create your views here.

def home_view(request):
    sendmail.delay()
    debug_task.delay()
    return HttpResponse("Hello, my home view")
