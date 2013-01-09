#coding=utf-8

from uliweb.form import *

class siteinfoForm(Form):
        name   = StringField(label="站点名称",required=True)
        url    = StringField(label="域名")
        desc   = TextField(label="简短描述",required=True,rows=5,cols=30)
        #title  = StringField(label="站点名称")
        temp   = StringField(label="模板名称")
        logo   = StringField(label="logo图片")

class categoryForm(Form):
        id_order = StringField(label="排序",default=0)
        name     = StringField(label="栏目名",required=True)
        temp     = StringField(label="模板名称")
        image    = StringField(label="图片")

class contentForm(Form):
        id_order = StringField(label="排序",default=0)
        cateid   = StringField(label="栏目序号")
        title    = StringField(label="标题",required=True)
        content  = TextField(label="内容",required=True,rows=10,cols=60)
        image    = StringField(label="图片")

class onlinecodeForm(Form):
        id_order = StringField(label="排序",default=0)
        cateid   = StringField(label="栏目序号",default=0)
        title    = StringField(label="标题",required=True)
        code     = StringField(label="代码地址",required=True)
        content  = TextField(label="内容",required=True,rows=10,cols=60)
        image    = StringField(label="图片")

