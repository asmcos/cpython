# range

`range` 用来产生一串连续整数，常和 `for` 一起用。

它包含起始值，不包含结束值。`range(0, 10)` 是 0 到 9。

Python 3 里 `range(...)` 本身不是列表。直接打印会看到一个 range 对象。若要看成列表，用 `list()` 包一层。

```
a = range(0, 10)
print(a)
print(list(a))

b = range(2, 4)
print(list(b))
```

## 执行结果

```
range(0, 10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[2, 3]
```

也可以只写一个参数：`range(5)` 相当于 `range(0, 5)`。第三个参数是步长：

```
print(list(range(0, 10, 2)))
```

结果是 `[0, 2, 4, 6, 8]`。
