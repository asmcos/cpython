# 文件处理

程序里的变量在程序结束时就没了。要让文字留下来，写进文件。这一节先用普通的 `open` 把读、写、指针和关闭说清楚，再用 `with ... as f` 把关闭交给 Python。

例子在 `examples/file_demo.py`。里面的 `test.txt` 这类文件是脚本自己创建的，跑完会删掉。

## 打开文件

~~~
f = open("test.txt", "w", encoding="utf-8")
~~~

`open` 是内置函数，不是新语法。它返回一个文件对象，这里叫 `f`。三个常用参数：

| 参数 | 作用 |
| --- | --- |
| 第一个，文件名 | 相对路径或绝对路径。`"test.txt"` 指当前目录里的这个文件 |
| 第二个，模式 | 读、写还是追加。不写时默认是 `"r"` |
| `encoding` | 文本按哪种编码解释。中文请写 `encoding="utf-8"` |

模式决定打开后能做什么，也决定文件指针一开始停在哪：

| 模式 | 含义 | 文件不存在 | 指针一开始 |
| --- | --- | --- | --- |
| `"r"` | 只读 | 报错 | 开头 |
| `"w"` | 只写。已有内容会被清空 | 新建 | 开头 |
| `"a"` | 追加，写到末尾 | 新建 | 末尾 |
| `"r+"` | 可读可写，不清空 | 报错 | 开头 |

末尾再加 `b` 就是二进制，例如 `"rb"`、`"wb"`。图片、压缩包用二进制，`read` 得到的是 `bytes`。普通文字不要加 `b`，用文本模式加上 `encoding`。

文件对象上能看到自己是怎么打开的：

~~~
print(f.name)
print(f.mode)
print(f.closed)
~~~

刚打开时 `f.closed` 是 `False`。`f.name` 是文件名，`f.mode` 是模式。

只用 `"r"` 去开一个还不存在的文件，会报错：

~~~
open("no_such.txt", encoding="utf-8")
~~~

~~~
FileNotFoundError: [Errno 2] No such file or directory: 'no_such.txt'
~~~

## write：写入

`write` 接收一个字符串，把它写到指针所在的位置，然后指针往后移。返回值是写进去的字符个数，不是字节数。

~~~
f = open("test.txt", "w", encoding="utf-8")
n = f.write("hello world\n")
print(n)
f.write("i am a boy\n")
f.write("i am very happy\n")
print(f.tell())
f.close()
~~~

~~~
12
39
~~~

`"hello world\n"` 是 11 个可见字符再加一个换行，所以 `write` 返回 12。三行都写完后，指针停在第 39 个字节。`\n` 是换行。

`writelines` 接收一个字符串列表，按顺序拼接写进去，**不会**自动给每一项加换行：

~~~
f = open("lines.txt", "w", encoding="utf-8")
f.writelines(["a", "b"])
f.close()
print(repr(open("lines.txt", encoding="utf-8").read()))
~~~

~~~
'ab'
~~~

想一行一个，列表里的字符串自己带上 `\n`。

`"w"` 会先把旧内容清掉。同一个文件再以 `"w"` 打开并写入，上次的内容就没了：

~~~
f = open("a.txt", "w", encoding="utf-8")
f.write("hello")
f.close()

f = open("a.txt", "w", encoding="utf-8")
f.write("world")
f.close()
~~~

文件里只剩下 `world`。不想清空，用 `"a"`。追加时指针一开始就在末尾，新内容接在后面：

~~~
f = open("a.txt", "a", encoding="utf-8")
print(f.tell())
f.write("!")
f.close()
~~~

~~~
5
~~~

`world` 是 5 个字符，所以一打开 `tell()` 就是 5。写完后文件内容是 `world!`。

## read：读取

`read` 从当前指针往后读。参数是最多读多少个字符；不写参数就读到文件末尾。

~~~
f = open("test.txt", encoding="utf-8")
print(repr(f.read(5)))
print(f.tell())
print(repr(f.readline()))
~~~

~~~
'hello'
5
' world\n'
~~~

`read(5)` 读 5 个字符，指针停在 5。紧接着的 `readline()` 从这里读到这一行结束，所以是 `' world\n'`，换行符还在字符串里。

再把指针拨回开头，可以读完全部：

~~~
f.seek(0)
text = f.read()
print(text)
print(repr(f.read()))
f.close()
~~~

~~~
hello world
i am a boy
i am very happy

''
~~~

第一次 `read()` 已经到了末尾，第二次没有新内容，得到空字符串。不是文件被删了，是指针停在末尾。

只要每一行，用 `readlines()`。它返回列表，每一项是一行，末尾的 `\n` 还保留着：

~~~
f = open("test.txt", encoding="utf-8")
lines = f.readlines()
print(lines)
f.close()
~~~

~~~
['hello world\n', 'i am a boy\n', 'i am very happy\n']
~~~

文件对象本身也可以放进 `for`，一次拿一行。打印前用 `strip()` 去掉行尾换行：

~~~
f = open("test.txt", encoding="utf-8")
for line in f:
    print(line.strip())
f.close()
~~~

~~~
hello world
i am a boy
i am very happy
~~~

大文件优先用 `for` 逐行读。`read()` 和 `readlines()` 会一次把整个文件放进内存。

## 指针：tell 和 seek

文件里有一个读写位置，叫做指针。`read` 和 `write` 都从指针处开始，做完就往后移。`tell()` 返回指针现在的位置。`seek(偏移, 从哪里算)` 把指针挪到新位置。

第二个参数可以不写，默认是 `0`：

| 第二个参数 | 从哪里算 |
| --- | --- |
| `0` | 文件开头 |
| `1` | 当前位置 |
| `2` | 文件末尾 |

~~~
f = open("test.txt", encoding="utf-8")
f.read(5)
pos = f.tell()
print(pos)

f.seek(0)
print(repr(f.read(5)))

f.seek(0, 2)
print(f.tell())

f.seek(pos)
print(repr(f.read(6)))
f.close()
~~~

~~~
5
'hello'
39
' world'
~~~

`seek(0)` 回到开头。`seek(0, 2)` 的偏移是 0、起点是末尾，所以指针到文件最后，`tell()` 是 39。`seek(pos)` 回到刚才记下的位置 5，再读 6 个字符就是 `' world'`。

文本模式下，`tell` 和 `seek` 按**字节**计，不是按字符。英文一个字符通常是 1 个字节，所以和 `read(5)` 对得上。中文在 UTF-8 里一个字常常是 3 个字节：

~~~
f = open("cn.txt", "w", encoding="utf-8")
print(f.write("你好"))
print(f.tell())
f.close()
~~~

~~~
2
6
~~~

`write` 说写了 2 个字符，`tell` 说指针在第 6 个字节。文本文件里不要凭感觉 `seek` 到“第几个字”。稳妥的做法是 `seek(0)` 回到开头，或者 `seek` 到某一次 `tell()` 返回的那个数。按字节随意跳动，用二进制模式 `"rb"`。

## close：关闭

用完要 `close()`。它做两件事：把还留在缓冲区里的内容真正写到磁盘，然后释放这个文件。

`write` 之后、`close` 之前，内容可能还没落到磁盘上。另一个 `open` 这时去读，会看到空的：

~~~
f = open("b.txt", "w", encoding="utf-8")
f.write("hello")

g = open("b.txt", encoding="utf-8")
print(repr(g.read()))
g.close()

f.close()

g = open("b.txt", encoding="utf-8")
print(repr(g.read()))
g.close()
~~~

~~~
''
'hello'
~~~

不想关闭、又想先把缓冲写出去，可以调用 `f.flush()`。日常写文件，关闭即可。

关闭之后 `f.closed` 变成 `True`。再读会报错：

~~~
print(f.closed)
f.read()
~~~

~~~
True
ValueError: I/O operation on closed file.
~~~

忘记 `close()` 时，少量数据可能一直留在缓冲里，程序异常退出后文件是空的或不完整。打开了很多文件却不关，也会占住系统的文件名额。

## with ... as f

每次都记得 `close()` 很容易漏，中间一报错，后面的 `close()` 就执行不到。`with` 把这件事包起来：进入缩进时打开，离开缩进时关闭，中间出错也会关。

~~~
with open("test.txt", encoding="utf-8") as f:
    data = f.read()

print(f.closed)
print(data)
~~~

~~~
True
hello world
i am a boy
i am very happy
~~~

`as f` 后面的 `f` 就是原来 `open` 返回的那个文件对象。缩进里照旧可以 `read`、`write`、`seek`。缩进一结束，文件已经关上，不必再写 `f.close()`。

写文件同样：

~~~
with open("a.txt", "w", encoding="utf-8") as f:
    f.write("hello")
~~~

`"w"` 仍会覆盖旧文件。只在末尾追加，第二个参数写 `"a"`。模式、`encoding`、`read`、`write`、`seek` 的规则和普通 `open` 完全一样，变的只是离开代码块时自动关闭。

以后读写真的文件，优先用 `with`。前面的 `open` / `close` 是为了看清每一步；看懂之后，新代码用 `with` 写。

## 路径

处理路径时，可以用标准库 `pathlib`：

~~~
from pathlib import Path

p = Path("test.txt")
print(p.exists())
print(p.read_text(encoding="utf-8"))
~~~

`exists()` 判断文件在不在。`read_text` 相当于打开、读完、关闭。入门先把 `open` 和 `with` 写熟。后面读写金融数据时，`Path` 会更方便。

## 常见坑

**`"w"` 会清空文件。** 原内容还要保留时用 `"a"`，或先读出来再写。

**读到空字符串。** 指针已经在末尾。再读之前 `seek(0)`。

**中文的 `seek` 不能按字数心算。** `tell` 是字节位置。回到开头用 `seek(0)`。

**`readlines` 的每一行带 `\n`。** 不要换行时用 `line.strip()`。

**不关闭，数据可能还在缓冲区。** 用 `with` 时离开缩进就会关闭。

## 小结

* `open(文件名, 模式, encoding="utf-8")` 打开文本文件
* `"r"` 读，`"w"` 写并清空，`"a"` 追加，`"r+"` 读写且不清空
* `write(字符串)` 返回字符数；`read()` 读到底，`read(n)` 读 n 个字符
* `tell()` 看指针，`seek(偏移, 从哪里算)` 移动指针
* `close()` 把缓冲写到磁盘并释放文件；关了再读会报错
* `with open(...) as f` 在离开缩进时自动关闭

下一节学习 [错误和异常](error_except.md)。用 `python examples/file_demo.py` 运行本节的例子。
