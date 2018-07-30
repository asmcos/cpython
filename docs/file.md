
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

# open 无参数 用法

```
f = open('a.txt')
```
打开一个文件,a.txt 必须存在，文件不存在的下面write再讲解。

# read

```
content = f.read()
```

读出所有的内容

现在内容都在content里面了。再调用read() 就没有内容了。

# readlines

```
f = open("a.txt")
lines = f.readlines()
for i in lines：
  print(i)
```
lines 格式是列表，每一行是一个列表成员。


# write

```
f = open("a.txt","w")
f.write("hello")
f.close()
```

写完了，必须关闭。一般调用关闭才能保存

open 第一个参数是 文件名称，第二个是"w",
* 表示可以写，
* 并且如果文件不存在会建立文件
* 如果文件存在，会覆盖老文件

如果要是打开可读写，不覆盖。 用"r+"参数

```
f = open("a.txt","r+")
f.write("world")
f.close()
```


#close

文件打开了，要是读写了。必须关闭

```
f.close()
```
