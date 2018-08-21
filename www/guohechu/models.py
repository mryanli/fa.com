# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.db import models

# Create your models here.

class Group(models.Model):

    apply_no = models.CharField(max_length=20,unique=True)
    department_made = models.CharField(max_length=20)
    mission_name = models.CharField(max_length=100)
    mission_background = models.CharField(max_length=300)
    mission_dest = models.CharField(max_length=200)
    group_category = models.CharField(max_length=20)
    group_xinshi = models.CharField(max_length=20)
    group_xiangmu = models.CharField(max_length=50)
    group_xiangmu_category = models.CharField(max_length=20)
    mission_country = models.CharField(max_length=15)
    mission_past_country = models.CharField(max_length=20)
    foreign_department = models.CharField(max_length=50)
    mission_path = models.CharField(max_length=40)
    group_peoples = models.IntegerField()
    mission_start_time = models.DateField()
    mission_end_time = models.DateField()
    fee_source = models.CharField(max_length=40)
    department_applied = models.CharField(max_length=30)
    apply_operator = models.CharField(max_length=10)
    group_operator = models.CharField(max_length=10)
    group_operator_tel = models.CharField(max_length=15)
    group_operator_fax = models.CharField(max_length=15)
    group_operator_leader = models.CharField(max_length=10)
    group_operator_leader_tel = models.CharField(max_length=15)
    group_operator_leader_fax = models.CharField(max_length=15)

    group_pijian_num = models.CharField(max_length=15)
    group_pijian_date = models.DateField()

    group_annotate = models.CharField(max_length=100)
    group_state = models.CharField(max_length=20)
    group_create_date = models.DateField(default=timezone.now)



class Member(models.Model):
    sort_num = models.IntegerField()
    name = models.CharField(max_length=10)
    pinyin = models.CharField(max_length=30)
    sex = models.BooleanField()
    birthday = models.DateField()
    birth_province = models.CharField(max_length=15)
    id_num = models.CharField(max_length=18)
    company = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    tel = models.CharField(max_length=15)
    fax = models.CharField(max_length=15)
    title = models.CharField(max_length=10)
    title_level = models.CharField(max_length=5)
    post = models.CharField(max_length=15)
    external_post = models.CharField(max_length=10)
    post_level = models.CharField(max_length=10)
    job = models.CharField(max_length=10)
    english_level = models.CharField(max_length=5)
    job_attribute = models.CharField(max_length=10)

    is_weiji = models.BooleanField(default=False)
    is_report = models.BooleanField(default=False)
    pass_port_id = models.ForeignKey('Passport',on_delete=models.DO_NOTHING)


class Passport(models.Model):
    num = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=15)
    pinyin = models.CharField(max_length=30)
    auth_date = models.DateField(default=timezone.now)
    expire_date = models.DateField(default=timezone.now)
    outin_state = models.CharField(max_length=10)  #正常借出、在库、销毁、寄往北京注销、随人员调离
    is_cancel = models.BooleanField(default= False) #已注销，未注销
    create_time = models.DateTimeField(default=timezone.now)
    create_operator = models.CharField(max_length=15,default='system')


class PassportOutIn(models.Model):
    outmenu_id = models.ForeignKey('Outmenu',on_delete=models.DO_NOTHING)
    passport_id = models.ForeignKey('Passport',on_delete=models.DO_NOTHING)
    in_time = models.DateTimeField(default=timezone.now)
    in_operator = models.CharField(max_length=15)


class Outmenu(models.Model):
    out_type = models.CharField(max_length=10) #正常借出、寄往北京注销、随人员调离、销毁
    out_why = models.CharField(max_length=30)
    out_time = models.DateTimeField(default=timezone.now)
    out_opertor = models.CharField(max_length=10)
    out_contactor = models.CharField(max_length=10)
    out_contact_tel = models.CharField(max_length=15)


class User(models.Model):
    name = models.CharField(max_length=10,unique=True)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=10)
    tel = models.CharField(max_length=15)
    department = models.CharField(max_length=20)






