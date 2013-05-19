#coding:utf-8

from uliweb.orm import *
import datetime

class content(Model):
	title    = Field(str)
	content  = Field(TEXT)
	image    = Field(str)
	cr_date  = Field(datetime.datetime,auto_now_add=True)	 
	up_date  = Field(datetime.datetime,auto_now_add=True)
	template = Field(str)
	order    = Field(int)
	status   = Field(str)
	cate_id  = Field(int)

class video (Model):
	title     = Field(str)
	content   = Field(TEXT)
	image     = Field(str)
	up_date   = Field(datetime.datetime,auto_now_add=True)
	template  = Field(str)
	order     = Field(int)
	course_id = Field(int)
	teacher   = Field(str)
	url       = Field(str)

class course (Model):
	name     = Field(str,max_length=255)
        desc     = Field(TEXT)
        image    = Field(str)
        template = Field(str)
        order    = Field(int)
        status   = Field(str)


class category(Model):
	name     = Field(str,max_length=255)	
	desc     = Field(TEXT)
	image    = Field(str)
	template = Field(str)
	order    = Field(int)
	status   = Field(str)
	

class siteinfo(Model):
	sitename = Field(str, max_length=255)
	logo     = Field(str)
	status   = Field(str)
