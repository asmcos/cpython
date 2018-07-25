# open

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
