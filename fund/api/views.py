# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from spider.tasks import sendmail


# Create your views here.

def home_view(request):
    sendmail.delay()
    return HttpResponse("Hello, home view")
