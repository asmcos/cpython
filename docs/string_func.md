#  字符串函数

字符串是python内置的类。我们可以直接使用，并且python已经内置了几个非常好用的函数


# 查看字符串的属性和方法

    ```
    >>> s = 'r'
    >>> print dir(s)
    ['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
    ```

# 如何使用这些方法

    通过dir()函数可以得到字符串对象的属性和方法, 但如何去查看怎么去使用它们呢？并不需要去网上搜索。

    ```
    >>> help(s.find)

    Help on built-in function find:

    find(...)
        S.find(sub [,start [,end]]) -> int

        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.

        Return -1 on failure.
    (END)
    ```

    以上就是通过了python 的help模块可以轻易的得到你想要的任何方法的使用文档。

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
