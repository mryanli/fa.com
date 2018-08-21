# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render,redirect
from .models import User

# Create your views here.


def index(req):
    return render(req,'guohechu/index.html',{'username':req.session['username']})


def login(req):
    if req.method =="GET":
        if req.session.get('is_login',None):
            return render(req,'guohechu/index.html',{'username':req.session['username']})
    errmsg = ''

    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']

        userobj = User.objects.filter(name=username)
        if  userobj:
            if password == userobj[0].password:
                req.session['is_login']=True
                req.session['username']=username
                return render(req,'guohechu/index.html',{'username':req.session['username']})



        errmsg = '用户名或密码错误，请重新输入'


    return render(req,'guohechu/login.html',{'errmsg':errmsg})


def logout(req):
    del req.session['is_login']
    del req.session['username']
    return render(req,'guohechu/login.html')

def passportlist(req):

    return render(req,'guohechu/passportlist.html',locals())
