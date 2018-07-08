# if
判断语句，常见的会和else 一起用。


### 例子1，判断调试是否成立，成立时打印

```
a = 5
if a > 1:
   print(a)
```

结果大家知道肯定是打印。

### 接下来讲缩进的语法块

```
a = 5
if a > 1:
   b = a
   print(b)

c = b
```

## 结果

```
5
```

上面的语句，中 b=a 和 print（b） 是根据if 条件成立的时候执行的，

而c=b 和if条件无关。

if条件语句 当条件成立后， 所有缩进的语句都会执行，直到 非缩进语句出现。

### 接下看一个例子

```
#coding:utf-8

a = 5

if a > 6:
   b = a
   print(b)

c = b

```

# 结果如何

```
Traceback (most recent call last):
  File "examples/if.py", line 9, in <module>
    c = b
NameError: name 'b' is not defined
```

## 为什么？错了！

提示b不存在，b为什么不存在？因为 a > 6不成立， 所以没有执行b=a

所以b不存在。
