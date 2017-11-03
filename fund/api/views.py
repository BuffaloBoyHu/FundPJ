# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse


# Create your views here.

def home_view(request):
    return HttpResponse("Hello, home view")
