#coding=utf-8
from uliweb import expose, functions
from models import *
from forms  import *
from uliweb.orm import get_model
from uliweb.utils.generic import *

def __begin__():
    from uliweb.contrib.auth.views import login
    if not request.user :
        return redirect(url_for(login) + '?next=/admin')
    elif request.user.is_superuser == False:
	return "Superman can operation the page!,sorry"

def common():
	cates     = category.all()
	return cates

def get_siteinfo():
	return siteinfo.all().one()

@expose('/admin')
def admin_index():
	data = {}
	site_info = siteinfo.all().one()
	if site_info:
		data = site_info.to_dict()

	sform     = siteinfoform(action="/admin/edit_siteinfo",data=data)
    	return {"sform":sform}

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
    	return {'cform':cform}

@expose('/admin/content/new/<cate_id>')
def admin_content_new(cate_id):
	cform = contentform(action="/admin/content/create/0",data={'cate_id':cate_id})
    	return {'cform':cform}

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
    	return {'cform':cform}

@expose('/admin/category/<id>')
def admin_category_show(id):
	contents  = content.filter(content.c.cate_id == id) 
    	return {"contents":contents,"id":id}

@expose('/admin/category/edit/<id>')
def admin_category_edit(id):
	if request.method == "GET":
		data = category.get(category.c.id == id).to_dict()
		cform = categoryform(action="/admin/category/create/%s"%id,data=data)
    	return {'cform':cform}

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


@expose('/admin/course')
class  CourseView(object):
	def __init__(self):
		self.model=get_model('course')

	@expose('')
	def list(self):
		def name(value,obj):
			return obj.get_url("/admin/course/view","name")

		view = ListView(self.model,fields_convert_map={'name':name})
		return view.run()

	def add(self):	
		def get_url(id):
			return url_for(CourseView.view,id=id)
		view = AddView(self.model,ok_url=get_url)
		return view.run()

	def view(self, id):
        
        	obj = self.model.get_or_notfound(int(id))
        	view = DetailView(self.model, obj=obj)
        	return view.run()

     	def edit(self, id):
        
        	obj = self.model.get_or_notfound(int(id))
        	view = EditView(self.model, 
            		ok_url=url_for(CourseView.view, id=int(id)), 
            		obj=obj)
        	return view.run()
    
    	def delete(self, id):
        
        	obj = self.model.get_or_notfound(int(id))
        	view = DeleteView(self.model, obj=obj, 
            			ok_url=url_for(CourseView.view, id=int(id)),
            			use_delete_fieldname='deleted')
        	return view.run()

@expose('/admin/apply')
class  ApplyView(object):
	def __init__(self):
		self.model=get_model('Apply')

	@expose('')
	def list(self):
		def name(value,obj):
			return obj.get_url("/admin/apply/view","name")

		view = ListView(self.model,fields_convert_map={'name':name})
		return view.run()

	def add(self):	
		def get_url(id):
			return url_for(ApplyView.view,id=id)
		view = AddView(self.model,ok_url=get_url)
		return view.run()

	def view(self, id):
        
        	obj = self.model.get_or_notfound(int(id))
        	view = DetailView(self.model, obj=obj)
        	return view.run()

     	def edit(self, id):
        
        	obj = self.model.get_or_notfound(int(id))
        	view = EditView(self.model, 
            		ok_url=url_for(ApplyView.view, id=int(id)), 
            		obj=obj)
        	return view.run()
    
    	def delete(self, id):
        
        	obj = self.model.get_or_notfound(int(id))
        	view = DeleteView(self.model, obj=obj, 
            			ok_url=url_for(ApplyView.view, id=int(id)),
            			use_delete_fieldname='deleted')
        	return view.run()
