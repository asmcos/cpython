# for 循环

Python 用缩进来表示代码块，相当于其他语言的 `{}`。`for` 下面要缩进的那几行，才会被循环执行。

```
l1 = ["a", "b", "c"]
for i in l1:
    print(i)
```

## 结果

```
a
b
c
```

## 和下标一起用

```
l2 = ["2", "a", 1, "d"]
for i in range(0, 4):
    print(l2[i])
```

结果：

```
2
a
1
d
```

更常见的写法是直接遍历，不自己数下标：

```
for item in l2:
    print(item)
```

如果既要下标又要值，用 `enumerate`：

```
for i, item in enumerate(l2):
    print(i, item)
```
