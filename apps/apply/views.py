#coding=utf-8
from uliweb import expose
from models import Apply,course
from forms import *






@expose('/new/')
def new():
    form = ApplyForm()
		
    if request.method == 'GET':
		all_course = course.filter(course.c.status == True)
    		return {'form':form,'all_course':all_course}
    elif request.method == 'POST':
		flag = form.validate(request.params)
		if flag:
			n = Apply(**form.data)
			n.save()
			response.template = "new_ok.html"
			return {"id":n.id} 
		else:
    			return {"form":form}

@expose('/showapply')
def showapply():
    all= Apply.filter(Apply.c.status == True)	
    return {"all":all}

@expose('/showcourse/<id>')
def showcourse(id):
	c1 = course.filter(course.c.status == True).filter(course.c.id == id)
	return {'c1':c1}

