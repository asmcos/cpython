#coding=utf-8
from uliweb import expose, functions
from models import *
from forms  import *

def __begin__():
    from uliweb.contrib.auth.views import login
    if not request.user :
        return redirect(url_for(login) + '?next=/admin')
    elif request.user.is_superuser == False:
	return "只有管理员才能管理此页面"

def common():
	cates     = category.all()
	return cates


@expose('/admin')
def admin_index():
	data = {}
	site_info = siteinfo.all().one()
	if site_info:
		data = site_info.to_dict()

	sform     = siteinfoform(action="/admin/edit_siteinfo",data=data)
	cates= common()
    	return {"cates":cates,"sform":sform}

@expose('/admin/edit_siteinfo')
def edit_siteinfo():
	if request.method == "POST":
		f    = siteinfoform()
		flag = f.validate(request.params)
		if flag:
			if f.data["id"] == "":
				del f.data["id"]
			n    = siteinfo(**f.data)
			n.save()
	return redirect('/admin')


###################################
# category
################################## 

@expose('/admin/category/new')
def admin_category_new():
	cform = categoryform(action="/admin/category/create/0")
	cates = common()
    	return {"cates":cates,'cform':cform}

@expose('/admin/content/new/<cate_id>')
def admin_content_new(cate_id):
	cform = contentform(action="/admin/content/create/0",data={'cate_id':cate_id})
	cates = common()
    	return {"cates":cates,'cform':cform}

@expose('/admin/content/create/<id>')
def admin_content_create(id):
	if request.method == "POST":
		f = contentform(request.params)
		flag = f.validate(request.params)
		if flag:
			n = content(**f.data)
			if id != 0 :
				n.id = id
			n.save()
	return redirect('/admin')

@expose('/admin/content/edit/<id>')
def admin_content_edit(id):
	if request.method == "GET":
		data = content.get(content.c.id == id).to_dict()
		cform = contentform(action="/admin/content/create/%s"%id,data=data)
		cates = common()
    	return {"cates":cates,'cform':cform}

@expose('/admin/category/<id>')
def admin_category_show(id):
	cates     = common()
	contents  = content.filter(content.c.cate_id == id) 
    	return {"cates":cates,"contents":contents,"id":id}

@expose('/admin/category/edit/<id>')
def admin_category_edit(id):
	if request.method == "GET":
		data = category.get(category.c.id == id).to_dict()
		cform = categoryform(action="/admin/category/create/%s"%id,data=data)
		cates = common()
    	return {"cates":cates,'cform':cform}

@expose('/admin/category/create/<id>')
def admin_category_create(id):
	if request.method == "POST":
		f = categoryform(request.params)
		flag = f.validate(request.params)
		if flag:
			n = category(**f.data)
			if id != 0:
				n.id = id
			n.save()
	return redirect('/admin')
