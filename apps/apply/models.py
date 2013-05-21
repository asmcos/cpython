from uliweb.orm import *
import datetime 

class Apply(Model):
    name        = Field(str,max_length=64)
    qq          = Field(str,max_length=64)
    phone       = Field(str,max_length=64)
    email       = Field(str,max_length=128)
    workage     = Field(str,max_length=128)
    company     = Field(str,max_length=256)
    city        = Field(str,max_length=128)
    course_id   = Field(int)
    post_date   = Field(datetime.datetime, auto_now_add=True)
    status      = Field(bool)

    def get_url(self,url,name):
	return "<a href=%s/%d>%s</a>"%(url,self.id,getattr(self,name))

class course(Model):
	name        = Field(str,max_length=64)
	city        = Field(str,max_length=64)
	course_time = Field(str,max_length=64)
	teacher     = Field(str,max_length=64)
	address     = Field(str,max_length=256)
	desc        = Field(TEXT)
        status      = Field(bool)

	def get_url(self,url,name):
		return "<a href=%s/%d>%s</a>"%(url,self.id,getattr(self,name))
