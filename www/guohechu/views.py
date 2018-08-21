# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render

# Create your views here.


def index(req):
    return render(req,'guohechu/index.html')


def login(req):
    return render(req,'guohechu/login.html')
