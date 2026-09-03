# 常用内置函数

不需要 `import` 就能用的函数，叫做内置函数。入门阶段先记这些。

## 查看和转换

```
print(type(1))
print(len("hello"))
print(int("12"))
print(float("3.14"))
print(str(10))
print(bool(0), bool(1))
```

```
<class 'int'>
5
12
3.14
10
False True
```

`bool(0)`、空字符串 `""`、空列表 `[]` 都是 `False`。

## 数字

```
print(abs(-5))
print(round(3.14159, 2))
print(max(1, 9, 3))
print(min(1, 9, 3))
print(sum([1, 2, 3]))
```

```
5
3.14
9
1
6
```

算收益率、价格、总分时会经常用到。

## 遍历相关

```
print(list(range(3)))
print(list(enumerate(["a", "b"])))
print(list(zip([1, 2], ["a", "b"])))
```

```
[0, 1, 2]
[(0, 'a'), (1, 'b')]
[(1, 'a'), (2, 'b')]
```

`enumerate` 同时给出下标和值。`zip` 把两个序列一对一对配起来。

## 排序和判断

```
print(sorted([3, 1, 2]))
print(sorted(["banana", "apple"], key=len))
print(all([True, True, False]))
print(any([False, True, False]))
```

```
[1, 2, 3]
['apple', 'banana']
False
True
```

想看完整名单，在交互环境里输入 `dir(__builtins__)`，或打开官方文档的 Built-in Functions。
