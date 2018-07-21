# 字典 dict

```
In [8]: d={}

In [9]: d['a'] =1

In [10]: d['b'] =3

In [11]: print(d)
{'a': 1, 'b': 3}
```

定义了一个字典 d， 给字典添加一项，key为"a",value为1

再添加一项 key为“b”，value 为3

获取所有的keys
------------

```
d.keys()
```

结果为一个列表。

>参考一下代码


```
d = {}


d['a']    = 1
d['b']    = "hello"
d['name'] = "Jike"
d['age']  = 21


""" 第二段 """

for k in d.keys():
    """ key """
    print (k),
    """ value """
    print (d[k])
```


结果
----

```
a 1
age 21
b hello
name Jike
```


追加和删除
---------

```
b = {'g':[1,2,3],'a':2}

""" 这个有追加效果,相同的key会被覆盖掉 """
d.update(b)

print(d)


del d['b']
```

d update 了b之后，的就是 之前的内容加上后来b的内容，结果自己做一下实验看看

这里删除 是删除了  key ‘b’，而不是 {'g':[1,2,3],'a':2}

key 为b的内容 “hello”

最后结果如下：

```
{'a': 2, 'name': 'Jike', 'g': [1, 2, 3], 'age': 21}
```


字典支持 同时获取 k和v的方法


```
for k,v in d.items():
    print (k,v)
```
