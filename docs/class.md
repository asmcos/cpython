# 类

类是把数据和操作这些数据的函数放在一起的一种写法。用类可以让代码更整齐。

## 定义一个类

```
class JeapeSite:
    n = "demo"

    def get_name(self):
        return "jeapedu"
```

类里面可以有变量，也可以有函数。这些都不是必须的：

```
class Test:
    pass
```

`pass` 表示这里暂时什么都不写。

## 创建实例

```
a = JeapeSite()

print(a.n)
print(a.get_name())
```

`a` 叫做 `JeapeSite` 的实例。`self` 代表当前这个实例。

## 初始化函数

```
class JeapeSite1:
    n = "demo"

    def __init__(self):
        self.data = ["1", 2, 3, "456"]

    def get_name(self):
        return "jeapedu"

    def set_name(self, name):
        self.name = name


b = JeapeSite1()
print(b.data)

b.set_name("jeapedu1")
print(b.name)
```

`__init__` 在 `b = JeapeSite1()` 时自动执行。

## 初始化时传入参数

```
class JeapeSite2:
    def __init__(self, name):
        self.data = ["1", 2, 3, "456"]
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


c = JeapeSite2("jeapedu2")
print(c.get_name())

c.set_name("2jeapedu")
print(c.get_name())
```

创建对象时把名字传进去，以后也可以用 `set_name` 改掉。
