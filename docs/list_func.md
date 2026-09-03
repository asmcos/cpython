# 列表函数

列表可以追加、插入、删除。

## append

往末尾追加。

```
l = []
l.append(1)
l.append("3243")
l.append("a")
l.append(["good", "morning"])
print(l)
```

列表里可以同时放整数、字符串，甚至另一个列表。

```
[1, '3243', 'a', ['good', 'morning']]
```

## pop

删除并返回最后一个元素。

```
print(l.pop())
print(l)
```

```
['good', 'morning']
[1, '3243', 'a']
```

也可以写 `l.pop(0)`，删除指定下标。

## insert

在指定位置插入。

```
l.insert(2, "insss")
print(l)
```

```
[1, '3243', 'insss', 'a']
```

`insert` 可以选位置，`append` 只能加在最后。

## 其他常用方法

```
nums = [3, 1, 2]
print(len(nums))
print(sorted(nums))
nums.sort()
print(nums)
```

`len` 看长度。`sorted` 返回新列表，原来的不动。`sort` 会改原来的列表。
