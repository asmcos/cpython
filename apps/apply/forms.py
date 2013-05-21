#coding=utf-8
from uliweb.form import *
from uliweb import settings

class ApplyForm(Form):
    name      = StringField(label="姓名", required=True)
    qq        = StringField(label='qq',   required=True)
    phone     = StringField(label='手机号',  required=True)
    email     = StringField(label='邮箱', required=True)
    company   = StringField(label='公司/学校')
    workage   = StringField(label='工作时间')
    city      = StringField(label='所在城市',required=True)
    course_id = StringField(label="课程ID(必须填写数字)",required=True) 


