#coding:utf-8

d = {}


d['a']    = 1
d['b']    = "hello"
d['name'] = "Jike"
d['age']  = 21

print(d)

""" 第二段 """

for k in d.keys():
    """ key """
    print (k),
    """ value """
    print (d[k])
