#coding:utf-8

from uliweb.form import *

class siteinfoform(Form):
        sitename   = StringField(label='站点名', required=True)
        logo       = StringField(label="logo")
	status     = StringField(label="状态")
	id         = HiddenField()

class categoryform(Form):
        name     = StringField(label="栏目名",required=True) 
        image    = StringField(label="栏目图片")
        template = StringField(label="栏目模版",default="")
        order    = StringField(label="显示顺序",default='0')
        status   = StringField(label="状态",default="开放")
        desc     = TextField(label="详细描述")

class contentform(Form):
        title    = StringField(label="标题",required=True) 
        image    = StringField(label="图片")
        url      = StringField(label="视频地址")
        template = StringField(label="模版",default="")
        order    = StringField(label="显示顺序",default='0')
        status   = StringField(label="状态",default="开放")
	cate_id  = StringField(label='栏目编号')
        content  = TextField(label="详细内容")
