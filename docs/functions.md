# 函数

把一段会重复使用的代码包起来，起个名字，就是函数。前面用过的 `print`、`len`、`enumerate` 都是 Python 自带的函数。这一节学自己写。

## 为什么需要函数

同一段打印写两遍，改格式时就要改两处：

~~~
print("*" * 5)
print("hello")
print("-" * 5)

print("*" * 5)
print("jeapedu")
print("-" * 5)
~~~

收成函数之后，格式只写一次。换内容时，只换调用时传进去的那个值。

## 定义和调用

~~~
def display(s):
    print("*" * 5)
    print(s)
    print("-" * 5)


display("hello")
display("jeapedu")
~~~

`def` 是定义。`display` 是函数名，后面的括号和冒号不能少。缩进的几行是函数体，调用时才执行。定义本身不会打印任何东西。

括号里的 `s` 是参数，是函数内部使用的名字。调用时写进括号的 `"hello"` 是传进去的值，会赋给 `s`。

`display("hello")` 的结果：

~~~
*****
hello
-----
~~~

`display("jeapedu")` 的结果：

~~~
*****
jeapedu
-----
~~~

函数名后面必须有括号。只写 `display` 不会执行函数体。

## 返回值

`print` 只是把内容显示出来。函数还可以用 `return` 把结果交回去，调用的地方再用这个结果。

~~~
def add(x, y):
    return x + y


print(add(1, 2))
~~~

~~~
3
~~~

`return` 一执行，函数就结束，后面的代码不会再跑。所以可以提前返回：

~~~
def label(score):
    if score >= 60:
        return "及格"
    return "不及格"


print(label(75))
print(label(40))
~~~

~~~
及格
不及格
~~~

没有写 `return` 的函数，调用结果是 `None`。`display` 负责打印，并不交出一个值：

~~~
result = display("hello")
print(result)
~~~

~~~
*****
hello
-----
None
~~~

屏幕上有字，只说明函数里执行了 `print`。外面的 `result` 仍然是 `None`。要让外面拿到计算结果，必须 `return`。

`return` 后面可以一次写多个值，实际上是交回一个元组。接收时用 [元组](tuple.md) 那一节的解包：

~~~
def divide(a, b):
    return a // b, a % b


print(divide(7, 2))
q, r = divide(7, 2)
print(q, r)
~~~

~~~
(3, 1)
3 1
~~~

`a // b` 是整除，`a % b` 是余数。7 除以 2 得到商 3、余 1。

## 多个参数和默认值

参数可以有好几个。没写默认值的，调用时必须传。写了默认值的，不传就用默认值。

~~~
def port(p=8080):
    print(f"port = {p}")


port()
port(80)
~~~

~~~
port = 8080
port = 80
~~~

~~~
def host(ip, port=8080):
    print(f"IP is {ip}:{port}")


host("127.0.0.1")
host("127.0.0.1", 80)
~~~

~~~
IP is 127.0.0.1:8080
IP is 127.0.0.1:80
~~~

`ip` 没有默认值，每次至少要传这一个。少传会报错：

~~~
host()
~~~

~~~
TypeError: host() missing 1 required positional argument: 'ip'
~~~

带默认值的参数要写在后面。下面这种定义是语法错误：

~~~
def host(port=8080, ip):
    print(ip, port)
~~~

~~~
SyntaxError: parameter without a default follows parameter with a default
~~~

调用时也可以写上参数名，叫关键字参数。名字对上即可，顺序可以和定义时不同：

~~~
host("127.0.0.1", port=80)
host(port=80, ip="127.0.0.1")
~~~

两行都打印 `IP is 127.0.0.1:80`。参数一多，写出名字比只靠位置更不容易传错。

## 函数内外的名字

函数里新起的名字，只在函数里面存在。

~~~
def add(x, y):
    total = x + y
    return total


print(add(1, 2))
print(total)
~~~

~~~
3
NameError: name 'total' is not defined
~~~

参数也是函数自己的名字。外面有一个 `n`，函数里再写 `n = n + 1`，改的是里面的那一个，外面的数字不变：

~~~
n = 10

def change(n):
    n = n + 1
    return n


print(change(n))
print(n)
~~~

~~~
11
10
~~~

传进去的如果是列表，函数里用 `append` 改的是同一份列表，外面能看到：

~~~
nums = [1, 2]

def append_three(items):
    items.append(3)


append_three(nums)
print(nums)
~~~

~~~
[1, 2, 3]
~~~

数字、字符串不能在原地修改，函数里的赋值只影响内部的名字。列表可以原地修改，传进去之后两边看到的是同一份。

## 参数个数不固定

参数前面加 `*`，多出来的位置参数会收成一个元组。一个都不传时，这个元组是空的。

~~~
def total(*nums):
    result = 0
    for n in nums:
        result = result + n
    return result


print(total(10, 20, 30))
print(total())
~~~

~~~
60
0
~~~

参数前面加 `**`，则把 `名字=值` 收成一个字典：

~~~
def show(**info):
    print(info)


show(name="Jike", age=20)
~~~

~~~
{'name': 'Jike', 'age': 20}
~~~

入门先把普通参数、默认值和 `return` 写熟。读到别人代码里的 `*args`、`**kwargs`，就是这两种收集方式，名字可以自己起，`*` 和 `**` 才是关键。

## 常见坑

**打印了，却没有返回。** 函数里只有 `print` 时，外面接到的是 `None`，不能拿去继续计算。需要结果就写 `return`。

**默认可变参数只创建一次。** 默认值在定义函数时就算好，不是每次调用重新做一个新列表。

~~~
def add_item(item, bucket=[]):
    bucket.append(item)
    return bucket


print(add_item(1))
print(add_item(2))
~~~

~~~
[1]
[1, 2]
~~~

两次调用用的是同一个 `bucket`，所以 2 被追加进了已经有 1 的列表。需要“每次都是空列表”时，默认值写成 `None`，在函数里面再创建：

~~~
def add_item(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


print(add_item(1))
print(add_item(2))
~~~

~~~
[1]
[2]
~~~

**少传了没有默认值的参数。** 报 `TypeError`，信息里会写出缺少的名字。

**带默认值的参数写在了前面。** 定义时就会 `SyntaxError`，函数还没机会被调用。

## 小结

* `def` 定义函数，调用时才执行函数体
* 参数是函数内部的名字，调用时把值传进去
* `return` 把结果交回去，并立刻结束函数；不写 `return` 时结果是 `None`
* 一次 `return` 多个值，得到的是元组
* 没默认值的参数放前面，调用时也可以用 `名字=值`
* 函数内部的新名字外面看不见；列表这类对象可以在函数里被原地修改
* 默认参数不要用 `[]`、`{}` 这种会变的值

下一节学习 [模块](module.md)。用 `python examples/functions.py` 运行本节的例子。
