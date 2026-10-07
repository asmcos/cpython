# 字符串

字符串是一段文字，类型是 `str`。用单引号或双引号包起来都可以。

```
s1 = "hello"
s2 = 'jeapedu'
print(s1, s2)
print(type(s1))
```

```
hello jeapedu
<class 'str'>
```

Python 3 默认 UTF-8，可以直接写中文。字符串是只读的：能取出某一个字符、切出一段、拼出新的，但不能改原来那个位置上的字。

常用方法（`split`、`strip`、`find` 等）放在下一节 [字符串函数](string_func.md)。这一节先把写法、下标、拼接和切片练熟。

## 三种写法

单引号、双引号没有功能差别。里面要出现同一种引号时，换另一种，或加反斜杠：

```
print("It's easy")
print('他说："你好"')
print('It\'s easy')
```

```
It's easy
他说："你好"
It's easy
```

第一行用双引号包起来，里面的单引号可以直接写。第二行反过来，用单引号包起来，里面的双引号可以直接写。第三行和第一行打印结果一样，单引号前面的 `\` 只是告诉 Python：这个 `'` 是文字，不是字符串的结尾。

三引号可以写多行：

```
text = """第一行
第二行"""
print(text)
```

前面加 `r` 表示原始字符串，反斜杠不再当转义，后面正则会用到：

```
print(r"C:\new\test")
```

## 下标：取出某一个字符

下标从 0 开始。`-1` 是最后一个，`-2` 是倒数第二个。

```
s = "abcdef"

print(s[0])
print(s[3])
print(s[-1])
print(s[-2])
```

```
a
d
f
e
```

下标超出长度会报 `IndexError`：

```
print(s[10])
```

## 字符串不能按位置修改

```
s = "abcdef"
s[0] = "1"
```

```
TypeError: 'str' object does not support item assignment
```

这不是写错了变量名，而是字符串本身不允许改其中某一个字符。要「改」，只能拼出一条新的：

```
s = "abcdef"
s2 = "1" + s[1:]
print(s2)
```

```
1bcdef
```

`s` 还是原来的 `abcdef`，`s2` 才是新字符串。

## 拼接和重复

`+` 把两段文字接起来。`*` 把同一段重复若干次。

```
print("jeape" + "du")
print("ha" * 3)

name = "Ana"
print("你好，" + name)
```

```
jeapedu
hahaha
你好，Ana
```

字符串不能直接和数字相加，会报 `TypeError`。先转成字符串，或用 f-string：

```
n = 3
print("第" + str(n) + "课")
print(f"第{n}课")
```

```
第3课
第3课
```

`f"..."` 在 [变量](variables.md) 里已经用来控制小数位。这里同样可以把变量嵌进文字。

## 长度和包含

`len(s)` 是字符个数。`in` 判断一段是否出现在里面。

```
s = "hello"
print(len(s))
print("ell" in s)
print("xyz" in s)
```

```
5
True
False
```

中文一个字也占一个下标：`len("你好")` 是 `2`。

## 切片：取出一段

切片写法是 `s[起点:终点]`。包含起点，**不包含**终点。和列表、元组的写法一样，[切片](slice.md) 一节会再汇总。

```
s = "abcdefghijkl"

print(s[1:5])
print(s[:5])
print(s[5:])
print(s[:])
```

```
bcde
abcde
fghijkl
abcdefghijkl
```

起点不写表示从开头，终点不写表示到末尾。终点写得比长度大，也只取到尾巴，不会报错。

第三个参数是步长：隔几个取一个。步长为 `-1` 可以从后往前。

```
print(s[0:5:2])
print(s[::-1])
```

```
ace
lkjihgfedcba
```

`s[::-1]` 是把整串倒过来，很常用。步长、反序的细节见 [切片](slice.md)。

## 转义字符

反斜杠表示特殊字符：

| 写法 | 含义 |
| --- | --- |
| `\n` | 换行 |
| `\t` | 制表符（对齐用的空格） |
| `\\` | 一个真正的反斜杠 |
| `\'` `\"` | 引号本身 |

```
print("第一行\n第二行")
```

路径里的 `\` 容易踩坑，Windows 路径建议写成 `r"C:\Users\name"`，或用正斜杠。

## 综合例子

```
s = "abcdef"

print(s[0], s[-1])
print("jeape" + "du")
print(s[1:5])
print(len(s), "cd" in s)
print(f"{s} 的长度是 {len(s)}")
```

```
a f
jeapedu
bcde
6 True
abcdef 的长度是 6
```

拆开、去空格、查找、替换，见下一节 [字符串函数](string_func.md)。

用 `python examples/string_demo.py` 运行本节的例子。
