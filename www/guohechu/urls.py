#!/usr/bin/python
# -*- coding:UTF-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url('index', views.index,name='index'),
    url('login',views.login,name='login'),
    url('logout',views.logout,name='logout'),
    url('passportlist',views.passportlist,name='passportlist'),
]