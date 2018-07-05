# coding:utf-8

"""
创建元组
"""

t1 = (1, 2, 3)

"""
如何读取元组
"""

t1 = (1, 2, 3, "a")

print "t1[0]: %s" % str(t1[0])

print "t1[-1]: %s" % str(t1[-1])

print "t1[2:4]: %s" % str(t1[2:4])

"""
合并元组
"""

t1 = (1, 2)
t2 = (3, 4)

t3 = t1 + t2

print t3

"""
删除元组
"""

t = (1,)

del t

"""
元组与列表的转换
"""

l = [1, 2, 3]

l = tuple(l)

print type(l)

t = (1, 2, 3)

t = list(t)

print type(t)