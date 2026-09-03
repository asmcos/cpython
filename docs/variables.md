# 变量

变量就是给一个值起名字，后面用这个名字来使用它。

Python 里常见的基础类型：

* `int`：整数，例如 `1`
* `float`：小数，例如 `3.14`
* `str`：字符串，例如 `"abc"`
* `bool`：真或假，`True` / `False`

## 例子

```
a = 1
b = 2
s1 = "abc"

print(a, b, s1)

s2 = str(a)
print(s2)

s3 = "435"
c = int(s3)

print(c + a)

print(type(a), type(s1))
```

`str(a)` 把数字变成字符串。`int(s3)` 把数字形式的字符串变成整数。`type()` 用来查看类型。

## 执行结果

```
1 2 abc
1
436
<class 'int'> <class 'str'>
```

注意：Python 3 里 `print(a, b, s1)` 打印的是 `1 2 abc`，不会再出现 Python 2 那种带括号的元组样子。

用 `python examples/variables.py` 可以自己跑一遍。
