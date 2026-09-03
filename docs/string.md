# 字符串

字符串是一段文字。它是只读的，不能改其中某一个字符。

下标从 0 开始。`-1` 表示最后一个字符。

```
s1 = "abcdef"

print(s1[0])
print(s1[3])

print("字符串的最后一个是：")
print(s1[-1])

# 这一句会出错，因为字符串不可以修改
s1[0] = "1"
```

## 执行结果

```
a
d
字符串的最后一个是：
f
Traceback (most recent call last):
  File "examples/string.py", line 12, in <module>
    s1[0] = "1"
    ~~~~^^^
TypeError: 'str' object does not support item assignment
```

最后一行报错是正常的。字符串不能按位置赋值。如果要改内容，需要生成新的字符串，例如：

```
s2 = "1" + s1[1:]
print(s2)
```

结果是 `1bcdef`。切片会在后面专门讲。
