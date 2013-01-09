#coding=utf-8

from uliweb.orm import *

class siteinfo(Model):
	name   = Field(str, max_length=255)
	url    = Field(str, max_length=255)
	desc   = Field(str, max_length=1024)
#	title  = Field(CHAR)
	temp   = Field(str, max_length=255)
	logo   = Field(str, max_length=255)

class category(Model):
	id_order = Field(int)
	name     = Field(str, max_length=255)
	num      = Field(int)
	temp     = Field(str, max_length=255)
	image    = Field(str, max_length=255)

class content(Model):
	id_order = Field(int)
	cateid   = Field(int)
	title    = Field(str, max_length=255)
	content  = Field(TEXT)
	image    = Field(str, max_length=255)


class onlinecode(Model):
	id_order = Field(int)
	cateid   = Field(int)
	title    = Field(str, max_length=255)
	content  = Field(TEXT)
	code     = Field(str,max_length=4096)
	image    = Field(str, max_length=255)



