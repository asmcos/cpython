#coding=utf-8
from uliweb import expose, functions
from admin.models import *
from admin.views import common


@expose('/')
def index():
    cates = common()
    site_info = siteinfo.all().one()
    return {'cates':cates,'site_info':site_info}


def get_category_by_order(orderid):
	contents = []
	cate     = category.get(category.c.order == orderid)
	if cate:
		contents = content.filter(content.c.cate_id == cate.id).limit(10)
	return contents,cate
