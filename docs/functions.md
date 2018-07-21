# 函数

>定义和使用

```
""" 定义一个新函数 """

def display (s):
    print("*" * 5)
    print(s)
    print("-" * 5)


""" 调用函数 """

display ("hello")

display ("cpython")
```

代码中定义了一个函数display ,括号里面的 s,是参数

下面用了2个调用的例子， 第一个例子传递了参数 "hello"
执行的时候 执行的时候 hello会被传到 print(s) 里面替换 s

执行结果
-------

>display("hello")

```
*****
hello
-----

```

> display("cpython") 执行的结果
```
*****
cpython
-----
```


默认参数的例子
------------

```
""" 默认参数 """

def port (p=8080):
    print("port = %d" % p)


port()

port(80)
```

当函数使用了默认参数时，调用的时候可以传递参数，也可以不传参数
上面分别写了2个例子。


更多参数例子
----------

```
def host(ip,port=8080):
    print("IP is %s:%d" % (ip,port))

host("127.0.0.1")

host("127.0.0.1",80)
```

当函数有2个参数时，第一个参数ip没有默认参数，

每次调用的时候就至少要传递一个参数。
