# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import User, Passport,Outmenu,PassportOutIn


# Create your views here.

#主界面
def index(req):
    return render(req, 'guohechu/passport/index.html', {'username': req.session['username']})

#登录界面
def login(req):
    if req.method == "GET":
        if req.session.get('is_login', None):
            return render(req, 'guohechu/passport/index.html', {'username': req.session['username']})
    errmsg = ''

    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']

        userobj = User.objects.filter(name=username)
        if userobj:
            if password == userobj[0].password:
                req.session['is_login'] = True
                req.session['username'] = username
                return render(req, 'guohechu/passport/index.html', {'username': req.session['username']})

        errmsg = '用户名或密码错误，请重新输入'

    return render(req, 'guohechu/login.html', {'errmsg': errmsg})

#登出
def logout(req):
    del req.session['is_login']
    del req.session['username']
    return render(req, 'guohechu/login.html')

#获取护照列表
def passportlist(req):
    passports = Passport.objects.all().order_by('-create_time')[0:10]
    data = {'username': req.session['username'],
            "passports": passports
            }
    return render(req, 'guohechu/passport/passportlist.html', data)

#添加护照
def addpassport(req):
    if req.method == 'POST':
        num = req.POST['num']
        name = req.POST['name']
        pinyin = req.POST['pinyin']
        sex = req.POST['sex']
        auth_date = req.POST['auth_date']
        expire_date = req.POST['expire_date']
        annotate = req.POST['annotate']

        print(name, pinyin, sex, auth_date, expire_date, annotate)
        Passport.objects.create(name=name, pinyin=pinyin, num=num, sex=sex,
                                auth_date=auth_date, expire_date=expire_date,
                                annotate=annotate, outin_state='在库')
        return redirect('guohechu/passport/passportlist.html', req.session['username']);

    return render(req, 'guohechu/passport/addpassport.html', {'username': req.session['username']})

#删除护照
def delpassport(req, id):
    Passport.objects.filter(id=id).delete()
    return redirect('guohechu/passport/passportlist.html', {'username': req.session['username']})

#编辑护照
def editpassport(req, id):
    if req.method == 'POST':
        edit_dict = {
            'num': req.POST['num'],
            'name': req.POST['name'],
            'pinyin': req.POST['pinyin'],
            'sex': req.POST['sex'],
            'auth_date': req.POST['auth_date'],
            'expire_date': req.POST['expire_date'],
            'annotate': req.POST['annotate']
        }

        Passport.objects.filter(id=id).update(**edit_dict)
        return redirect('guohechu/passport/passportlist.html', {'username': req.session['username']})


    passport = Passport.objects.get(id=id)
    print(passport.expire_date)

    return render(req, 'guohechu/passport/editpassport.html', {'username': req.session['username'], 'passport': passport})

#护照借出清单
def borrowlist(req):
    outmenu = Outmenu.objects.all().order_by('-out_time')[0:10]

    return render(req,'guohechu/borrow/borrowlist.html',{'username': req.session['username'],'outmenu':outmenu})


#添加护照时返回的界面
def addborrow(req):


    return render(req,'guohechu/borrow/addborrow.html',{'username': req.session['username']})


def borrow_add_passports(req):

    passports = Passport.objects.all().order_by('-create_time')[0:10]
    return render(req,'guohechu/borrow/borrow_add_passports.html',{'passports':passports})