# 字符串函数

上一节 [字符串](string.md) 讲了下标、拼接和切片。这一节用字符串自带的方法做拆分、去掉空白、查找和替换。

在交互环境里可以列出全部方法，也可以查某一个怎么用：

```
>>> s = "hello"
>>> print(dir(s))
>>> help(s.find)
```

入门先会下面几个。

## split：按分隔符拆开

```
s = "Whether you're new to programming or an experienced developer, it's easy to learn and use Python."
print(s.split(" "))
```

```
['Whether', "you're", 'new', 'to', 'programming', 'or', 'an', 'experienced', 'developer,', "it's", 'easy', 'to', 'learn', 'and', 'use', 'Python.']
```

这段话来自 python.org。按空格拆开，得到一个列表。处理日志、CSV 粗分列时很常见。不写参数时，`split()` 会按空白拆，并自动去掉多余空格。

## strip：去掉两端空白

```
s1 = "  good   "
print(s1)
print(s1.strip())
```

```
  good
good
```

只去左边用 `lstrip()`，只去右边用 `rstrip()`。中间的空格不会去掉。

## join：把列表拼回字符串

```
parts = ["04", "f4", "03", "e2", "54", "76", "10"]
print("-".join(parts))
```

```
04-f4-03-e2-54-76-10
```

注意是 **分隔符**.join(列表)，不是 `列表.join(分隔符)`。

## find：查找子串

返回第一次出现的下标。找不到返回 `-1`。

```
s = "fdsa"
print(s.find("a"))
print(s.find("s"))
print(s.find("z"))
```

```
3
2
-1
```

`in` 只回答有没有，`find` 还能告诉你在第几位。

## replace：替换

```
s = "hello python"
print(s.replace("python", "jeapedu"))
```

```
hello jeapedu
```

原来的 `s` 不变，`replace` 返回新字符串。

## 大小写

```
s = "Hello Python"
print(s.lower())
print(s.upper())
```

```
hello python
hello PYTHON
```

比较用户输入时，常常先 `strip()` 再 `lower()`，避免空格和大小写干扰。

## 和 f-string 一起用

```
name = "Ana"
score = 92
print(f"{name} 的成绩是 {score}")
```

```
Ana 的成绩是 92
```

需要先加工再嵌进去：

```
raw = "  ana  "
print(f"你好，{raw.strip().title()}")
```

```
你好，Ana
```

列表上的 `append`、`pop` 见 [列表函数](list_func.md)。

用 `python examples/string_func_demo.py` 运行本节的例子。
