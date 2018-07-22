#coding:utf-8

class CPython:
    """ 简单的类实例 """
    n = "demo"

    def get_name(self):
        return "CPython"

a = CPython()

print(a.n)

print(a.get_name())

""" 初始化函数 """

class CPython1:
    """ 简单的类实例 """
    n = "demo"

    def __init__(self):
        self.data = ['1',2,3,"456"]

    def get_name(self):
        return "CPython"

    def set_name(self,name):
        self.name = name


b = CPython1()

print(b.data)

b.set_name("cpython1")
print(b.name)


"""带参数的初始化"""
class CPython2:
    """ 简单的类实例 """
    n = "demo"

    def __init__(self,name):
        self.data = ['1',2,3,"456"]
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name

c = CPython2("cpython2")

print(c.get_name())

c.set_name("2cpython")

print(c.get_name())
