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

b = {'g':[1,2,3],'a':2}

""" 这个有追加效果,相同的key会被覆盖掉 """
d.update(b)

print(d)


del d['b']

print(d)

for k,v in d.items():
    print (k,v)
