# if 判断

条件成立时执行缩进的代码。常常和 `else`、`elif` 一起用。

## 条件成立就打印

```
a = 5
if a > 1:
    print(a)
```

结果是 `5`。

## 缩进决定哪些语句属于 if

```
a = 5
if a > 1:
    b = a
    print(b)

c = b
print(c)
```

`b = a` 和 `print(b)` 只有条件成立才会执行。`c = b` 和 if 无关。

## 条件不成立会怎样

```
a = 5

if a > 6:
    b = a
    print(b)

c = b
```

结果：

```
Traceback (most recent call last):
  File "examples/if.py", line 8, in <module>
    c = b
NameError: name 'b' is not defined
```

`a > 6` 不成立，所以没有执行 `b = a`，后面使用 `b` 就会报错。

## else 和 elif

```
score = 75

if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

结果是 `及格`。

## Python 3.10 起可以用 match

3.12 也可以用 `match / case`，适合拿一个值去匹配几种情况：

```
op = "+"

match op:
    case "+":
        print(1 + 2)
    case "-":
        print(1 - 2)
    case _:
        print("未知运算")
```

入门阶段把 `if / elif / else` 写熟即可。`match` 以后见到能看懂就行。
