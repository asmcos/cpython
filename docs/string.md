# 字符串
python 里面的字符串是一个实例,字符串是只读的，不可以修改。

# 字符串下标

```
#coding:utf-8

s1 = "abcdef"

print(s1[0])

print(s1[3])

"""
注释，字符串最后一个字符 这里是f
"""

print('字符串的最后一个是：')
print(s1[-1])

"""
这一句执行会出错，因为字符串不可以修改
"""
s1[0] = '1'

```

# 执行结果

```
jeapedudeAir-3:docs jeapedu$ python ../examples/string.py
a
d
字符串的最后一个是：
f
Traceback (most recent call last):
  File "../examples/string.py", line 19, in <module>
    s1[0] = '1'
TypeError: 'str' object does not support item assignment
```
