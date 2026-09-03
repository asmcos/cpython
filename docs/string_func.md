# 字符串函数

字符串是 Python 内置类型，自带一批常用方法。

## 查看有哪些方法

在交互环境里：

```
>>> s = "hello"
>>> print(dir(s))
```

会列出很多名字。下面这些入门阶段最常用。

不知道某个方法怎么用时，用 `help`：

```
>>> help(s.find)
```

不必先去网上搜。

## split

按分隔符把字符串拆成列表。

```
s = "Whether you're new to programming or an experienced developer, it's easy to learn and use Python."
print(s.split(" "))
```

结果：

```
['Whether', "you're", 'new', 'to', 'programming', 'or', 'an', 'experienced', 'developer,', "it's", 'easy', 'to', 'learn', 'and', 'use', 'Python.']
```

这段话来自 python.org。按空格拆开，在处理日志、CSV 粗分列时很常见。

## strip

去掉两端空白。

```
s1 = "  good   "
print(s1)
print(s1.strip())
```

```
  good
good
```

## join

把列表拼成一个字符串。

```
l = ["04", "f4", "03", "e2", "54", "76", "10"]
print("-".join(l))
```

```
04-f4-03-e2-54-76-10
```

## find

查找子字符串，返回第一次出现的下标。找不到返回 `-1`。

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

## replace 和 f-string

```
s = "hello python"
print(s.replace("python", "jeapedu"))

name = "Ana"
score = 92
print(f"{name} 的成绩是 {score}")
```

```
hello jeapedu
Ana 的成绩是 92
```
