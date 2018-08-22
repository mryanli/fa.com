# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render,redirect
from .models import User,Passport

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
    passports = Passport.objects.all()[0:10]
    data = {'username':req.session['username'],
            "passports":passports
            }
    return render(req,'guohechu/passportlist.html',data)


def addpassport(req):

    if req.method =='POST':

        num = req.POST['num']
        name =  req.POST['name']
        pinyin = req.POST['pinyin']
        sex = req.POST['sex']
        auth_date = req.POST['auth_date']
        expire_date = req.POST['expire_date']
        annotate = req.POST['annotate']

        print(name,pinyin,sex,auth_date,expire_date,annotate)
        Passport.objects.create(name=name,pinyin=pinyin,num = num,sex=sex,
                                auth_date=auth_date,expire_date=expire_date,
                                annotate=annotate,outin_state='在库')
        return redirect('guohechu/passportlist.html',req.session['username']);

    return render(req,'guohechu/addpassport.html',{'username':req.session['username']})


def delpassport(req,id):
    Passport.objects.filter(id = id).delete()
    return redirect('guohechu/passportlist.html',{'username':req.session['username']})


def editpassport(req,id):
    passport = Passport.objects.get(id = id)
    print(passport.expire_date)

    return render(req,'guohechu/editpassport.html',{'username':req.session['username'],'passport':passport})