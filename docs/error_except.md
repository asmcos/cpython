# 错误异常

```
In [1]: int("567")
Out[1]: 567

In [2]: int("56fdsa7")
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-2-bb997a28a2f4> in <module>()
----> 1 int("56fdsa7")

ValueError: invalid literal for int() with base 10: '56fdsa7'

```

int() 函数可以把 字符串“567”转换成数字 567，
但是如果如果遇到了非数字的字符串转换就会 出问题。 见上面代码。

```

try:

except:

```

这是专门用来解决此问题的方法。

用法如下：
-------

```
In [4]: try :
    int("56fdsa7")
except:
    print("hahaha")
   ...:     
hahaha
```

这时候系统不会因为错误而退出，反而我们可以获取 错误。

当我们不确认是否能够正确执行的语句都可以放在 try： 模块。

如果执行异常就会 执行 except： 后面的模块。
如果执行正确，except 就不会被执行。
