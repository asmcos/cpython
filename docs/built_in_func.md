# 常用内置函数

不需要 `import` 就能用的函数，叫做内置函数。入门阶段先记这些。算价格、收益率、汇总数据时会经常用到。

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

读金融数据时，字符串常需要转成数字：`int("12")`、`float("3.14")`。反过来要打印拼接时，用 `str(10)`。

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

`round(数字, 位数)` 四舍五入到指定位数。`sum` 用来累加列表里所有数，比如算一段时间的总成交额。

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

`enumerate` 是内置函数，同时给出下标和值，详见 [for 循环](for.md)。`zip` 把两个序列一对一对配起来，比如把日期和收盘价配成一对对。

## 类型判断：isinstance

`isinstance(值, 类型)` 判断一个值是不是某种类型，返回 `True` / `False`：

```
print(isinstance(12, int))
print(isinstance("12", int))
print(isinstance(3.14, float))
```

```
True
False
True
```

读取的数据常常类型不确定，判断后再处理比较稳妥：

```
def fmt(v):
    if isinstance(v, (int, float)):
        return round(v, 2)
    return v


print(fmt(3.14159))
print(fmt("abc"))
```

```
3.14
abc
```

`isinstance(v, (int, float))` 里的括号表示"是 int **或** float 之一"。

## 映射和过滤：map / filter

`map(函数, 列表)` 对列表里的每个元素调用这个函数，返回一个新列表：

```
prices = ["10.5", "11.2", "10.8"]
nums = list(map(float, prices))
print(nums)
```

```
[10.5, 11.2, 10.8]
```

这里把字符串价格列表批量转成浮点数。注意 `map` 返回的是一个可迭代对象，要用 `list()` 包起来才能直接看到列表。

`filter(函数, 列表)` 只保留函数返回 `True` 的元素：

```
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
```

```
[2, 4, 6]
```

`lambda x: x % 2 == 0` 是一个匿名小函数，意思是"x 能被 2 整除"。从一堆数据里筛出符合条件的记录时很常用。

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

`sorted` 返回排好序的**新列表**，不改原列表。`key=len` 表示按长度排。

`all` 全部为真才返回 `True`；`any` 只要有一个为真就返回 `True`。检查一批数据是否都满足条件时很常用，比如检查一组价格是否都大于 0。

## 金融场景：批处理价格

把一批字符串价格转成数字、筛选出高于 10 的、再求和：

```
prices = ["10.5", "9.8", "11.2", "10.8", "9.5"]
nums = list(map(float, prices))
above = list(filter(lambda x: x > 10, nums))
print(nums)
print(above)
print(sum(above))
```

```
[10.5, 9.8, 11.2, 10.8, 9.5]
[10.5, 11.2, 10.8]
32.5
```

## 小结

* 转换：`int()`、`float()`、`str()`、`bool()`
* 数字：`abs`、`round`、`max`、`min`、`sum`
* 遍历：`enumerate`（带下标）、`zip`（配对）
* 判断类型：`isinstance(值, 类型)`
* 批处理：`map`（逐个转换）、`filter`（筛选）
* 排序判断：`sorted`、`all`、`any`
* 想看完整名单，在交互环境里输入 `dir(__builtins__)`，或打开官方文档的 Built-in Functions

用 `python examples/built_in_func.py` 运行本节的例子。下一节学习 [调试](debug.md)。
