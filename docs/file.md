# 文件处理

python 对于文件的处理在我的工作当中会经常用到, 而且应用生活中有很大的用途, 今天我们讲对于文件的读写, 和一些容易碰到的错误。

# 读文件

open 函数
```
可以利用open函数创建一个file对象,调用file的相关方法进行文件的基础操作。

Help on built-in function open in module __builtin__:

open(...)
    open(name[, mode[, buffering]]) -> file object
    
    Open a file using the file() type, returns a file object.  This is the
    preferred way to open a file.  See file.__doc__ for further information.
(END)

上面是通过help函数得到关于open函数的描述。

name: 需要访问的文件名(可以指定相对和绝对地址)
mode: 文件的读取模式(读, 写, 追加等。)
buffering: 文件的寄存区(可以后续了解)

读取文件

test.txt内容如下
hello world
i am a boy
i am very happy

f = open('test.txt', 'r')
data = f.read()
f.close()

print (data)


```