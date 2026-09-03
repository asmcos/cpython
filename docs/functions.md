# 函数

把一段会重复使用的代码包起来，就是函数。

## 定义和调用

```
def display(s):
    print("*" * 5)
    print(s)
    print("-" * 5)


display("hello")
display("jeapedu")
```

括号里的 `s` 是参数。调用时传入的值会替换到函数里面。

`display("hello")` 的结果：

```
*****
hello
-----
```

`display("jeapedu")` 的结果：

```
*****
jeapedu
-----
```

## 默认参数

```
def port(p=8080):
    print(f"port = {p}")


port()
port(80)
```

有默认值的参数，调用时可以不传。上面两行分别打印 `port = 8080` 和 `port = 80`。

## 多个参数

```
def host(ip, port=8080):
    print(f"IP is {ip}:{port}")


host("127.0.0.1")
host("127.0.0.1", 80)
```

`ip` 没有默认值，每次至少要传这一个参数。

## 返回值

函数不只是打印，还可以把结果送回来：

```
def add(x, y):
    return x + y


print(add(1, 2))
```

结果是 `3`。
