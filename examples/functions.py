#coding:utf-8

""" 定义一个新函数 """

def display (s):
    print("*" * 5)
    print(s)
    print("-" * 5)


""" 调用函数 """

display ("hello")

display ("cpython")


""" 默认参数 """

def port (p=8080):
    print("port = %d" % p)


port()

port(80)


def host(ip,port=8080):
    print("IP is %s:%d" % (ip,port))

host("127.0.0.1")

host("127.0.0.1",80)
