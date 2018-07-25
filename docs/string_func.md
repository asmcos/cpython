#  字符串函数

字符串是python内置的类。我们可以直接使用，并且python已经内置了几个非常好用的函数

# split

```
s = "Whether you're new to programming or an experienced developer, it's easy to learn and use Python."

print(s.split(" "))

```

上面一段话来自python.org 。 我们用空格将其分开。

结果
----

```
['Whether', "you're", 'new', 'to', 'programming', 'or', 'an', 'experienced', 'developer,', "it's", 'easy', 'to', 'learn', 'and', 'use', 'Python.']
```

这个功能应用非常广泛。


# strip

```
s1 = "  good   "
print(s1)
print(s1.strip())
```
这个功能将字符串两端的 空白都除掉。


```
  good   
good
```

# join

连接，这个在实际编程的时候拼接非常好。

```
l = ['04','f4','03','e2','54','76','10']

print ("-".join(l))
```

结果

```
04-f4-03-e2-54-76-10
```


# find

```
In [7]: s = "fdsa"

In [8]: s.find("a")
Out[8]: 3

In [9]: s.find("s")
Out[9]: 2

```
在字符串中查找 某个子字符串，返回找到的位置。
找不到的时候返回 "-1"
