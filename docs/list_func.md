# 追加

```
l = []

l.append（1）
l.append("3243")
l.append("a")
```

列表里面可以同时存在 int类型和字符串，甚至包括子列表，字典。

```
l.append(['good',"morning"])
```

#结果

```
[1, '3243', 'a', ['good', 'morning']]
```

# pop

```
In [7]: l.pop()
Out[7]: ['good', 'morning']

In [8]: l
Out[8]: [1, '3243', 'a']
```

这样就把最后一个删除了，返回的结果是最后一个。
剩下了3个。


#insert

```
In [9]: l.insert(2,"insss")

In [10]: l
Out[10]: [1, '3243', 'insss', 'a']
```

又插入了一个，插入是可选择位置的，append是最后一个追加。
