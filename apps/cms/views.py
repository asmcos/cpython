#coding=utf-8
from uliweb import expose, functions
from admin.models import *


@expose('/')
def index():
    return {}


@expose('/showcontent/<id>')
def showcontent(id):
	c1 = content.get(content.c.id == id)
	if c1.template:
		response.template = c1.template	
	return {'c1':c1}

def get_category_by_order(orderid):
	contents = []
	cate     = category.get(category.c.order == orderid)
	if cate:
		contents = content.filter(content.c.cate_id == cate.id).limit(10)
	return contents,cate

