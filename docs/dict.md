# 字典 dict

字典用来保存「名字 → 值」。名字叫做 key，值叫做 value。

```
d = {}
d["a"] = 1
d["b"] = 3
print(d)
```

结果：

```
{'a': 1, 'b': 3}
```

## 遍历

Python 3 里 `d.keys()` 不是列表，而是一个视图。直接拿来循环即可：

```
d = {}
d["a"] = 1
d["b"] = "hello"
d["name"] = "Jike"
d["age"] = 21

for k in d.keys():
    print(k, d[k])
```

也可以一次取出 key 和 value：

```
for k, v in d.items():
    print(k, v)
```

## 追加和删除

```
b = {"g": [1, 2, 3], "a": 2}

d.update(b)
del d["b"]
print(d)
```

`update` 会把另一个字典合进来。相同的 key 会被后写入的值覆盖。`del d["b"]` 删除的是 key 为 `"b"` 的那一项。

## 执行结果（示例）

```
a 1
b hello
name Jike
age 21
{'a': 2, 'name': 'Jike', 'g': [1, 2, 3], 'age': 21}
```

字典在 Python 3.12 里默认按插入顺序排列。
