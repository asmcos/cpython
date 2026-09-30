# 错误和异常

有些代码不一定能执行成功。字符串里混进了字母，就不能转成整数：

~~~
print(int("567"))
print(int("56fdsa7"))
~~~

第一行得到 `567`。第二行程序停住，报错的最后一行是：

~~~
ValueError: invalid literal for int() with base 10: '56fdsa7'
~~~

不管这个错误，后面的代码就不会再执行。`try` / `except` 用来接住它，让程序换一条路继续走。

## 先把报错读完

单独运行上面第二行，完整报错是这样的：

~~~
Traceback (most recent call last):
  File "convert.py", line 2, in <module>
    print(int("56fdsa7"))
          ^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: '56fdsa7'
~~~

从下往上读：

* 最后一行是异常类型和说明。这里是 `ValueError`，意思是值的内容不合适
* 上面两行是出错的代码。`^^^^` 指着真正执行失败的那一段，也就是 `int("56fdsa7")`
* `File "convert.py", line 2` 是文件名和行号
* `Traceback` 是调用过程。函数套函数时，这里会有好几层，最下面一层是直接出错的位置

语法错误在运行前就被发现，例如少写冒号、缩进对不齐，类型常常是 `SyntaxError` 或 `IndentationError`。这种错误写在同一个文件的 `try` 里面也接不住，因为文件还没开始执行。下面讲的是程序已经跑起来之后才出现的异常。

## 常见的几类

| 类型 | 什么时候出现 |
| --- | --- |
| `ValueError` | 类型对，但值不合适，例如 `int("56fdsa7")` |
| `TypeError` | 类型不能这样用，例如 `1 + "3"` |
| `NameError` | 名字还没有定义 |
| `IndexError` | 下标超出列表范围 |
| `KeyError` | 字典里没有这个 key |
| `ZeroDivisionError` | 除数是 0 |
| `FileNotFoundError` | 要打开的文件不存在 |

各自的说明：

~~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
NameError: name 'no_such_name' is not defined
IndexError: list index out of range
KeyError: 'b'
ZeroDivisionError: division by zero
FileNotFoundError: [Errno 2] No such file or directory: 'no_such_file.txt'
~~~

`KeyError: 'b'` 表示字典里没有 `"b"` 这个 key。文件那一节的 `open("no_such.txt")` 报的就是 `FileNotFoundError`。怎么查这种报错，下一节 [调试](debug.md) 会再顺着讲。

## try / except

把可能出错的语句放进 `try`，出错时执行对应的 `except`：

~~~
try:
    print(int("56fdsa7"))
except ValueError:
    print("这不是一个整数")
~~~

~~~
这不是一个整数
~~~

程序不会退出。`try` 里如果没有出错，`except` 不会执行：

~~~
try:
    print(int("567"))
except ValueError:
    print("这不是一个整数")
~~~

~~~
567
~~~

`except` 后面写上具体类型。空的 `except:` 会把所有错误都吞掉，包括你打字打错造成的 `NameError`，排查时就像没报错一样。入门不要这样写。

要看原始说明，用 `as` 接住这个异常对象：

~~~
try:
    print(int("56fdsa7"))
except ValueError as e:
    print(type(e).__name__)
    print(e)
~~~

~~~
ValueError
invalid literal for int() with base 10: '56fdsa7'
~~~

`e` 是这次出错的对象。`type(e).__name__` 是类型名，直接打印 `e` 是冒号后面的那句说明。

同一种操作可能遇到不同的错，就写成多个 `except`，从上往下对上第一个就停：

~~~
def calc(text, divisor):
    try:
        n = int(text)
        return n / divisor
    except ValueError:
        print("不是整数")
    except ZeroDivisionError:
        print("除数是 0")


print(calc("10", 2))
calc("56fdsa7", 2)
calc("10", 0)
~~~

~~~
5.0
不是整数
除数是 0
~~~

## else 和 finally

`try` 也可以带 `else` 和 `finally`。`else` 只在 `try` 里没有出错时执行。`finally` 无论有没有出错都会执行，用来做收尾。

~~~
try:
    n = int("567")
except ValueError:
    print("这不是一个整数")
else:
    print("转换成功", n)
finally:
    print("收尾")
~~~

~~~
转换成功 567
收尾
~~~

转换失败时不会进 `else`，但 `finally` 仍会执行：

~~~
try:
    n = int("56fdsa7")
except ValueError:
    print("这不是一个整数")
else:
    print("转换成功", n)
finally:
    print("收尾")
~~~

~~~
这不是一个整数
收尾
~~~

打开文件后，无论中间有没有出错，都应该 `close`。可以放进 `finally`：

~~~
f = open("note.txt", "w", encoding="utf-8")
try:
    f.write("hello")
finally:
    f.close()

print(f.closed)
~~~

~~~
True
~~~

上一节的 `with open(...) as f` 就是把这件事写短了：离开 `with` 时一定会关闭，包括中途出错的情况。平时读写文件优先用 `with`。`finally` 留给别的必须收尾的动作。

## 自己抛出异常

发现数据不合法，可以用 `raise` 主动抛出异常，让调用的人用 `try` 去接：

~~~
def check_price(n):
    if n < 0:
        raise ValueError("价格不能是负数")
    return n


print(check_price(10))
~~~

~~~
10
~~~

~~~
check_price(-1)
~~~

~~~
ValueError: 价格不能是负数
~~~

`raise` 后面跟一个异常对象。类型要和问题相符：值不合适用 `ValueError`，文件没有用 `FileNotFoundError`。不要为了省事一律 `raise Exception`。

## 常见坑

**`except:` 什么都不写。** 连拼写错误也会被当成“处理过了”。至少写成 `except ValueError` 这种具体类型。

**父类型写在子类型前面。** `FileNotFoundError` 属于 `OSError`。先写 `except OSError`，后面的 `except FileNotFoundError` 永远走不到：

~~~
try:
    open("no_such_file.txt", encoding="utf-8")
except OSError:
    print("按 OSError 接住了")
except FileNotFoundError:
    print("文件不存在")
~~~

~~~
按 OSError 接住了
~~~

更具体的类型要写在前面。只想处理文件不存在时，直接 `except FileNotFoundError`。

**`try` 包得太大。** 把十几行都放进一个 `try`，就看不出是哪一句出的错。只包真正可能失败的那几句，例如转换、除法、打开文件。

## 小结

* 报错从最后一行读起：类型、说明，再看行号和 `^^^^` 指着的代码
* `try` 里出错才进入匹配的 `except`，程序可以继续
* `except 类型 as e` 能拿到这次错误的说明
* `else` 在没出错时执行，`finally` 总会执行
* 关闭文件优先用 `with`，不必自己在 `finally` 里 `close`
* `raise` 用来主动报告不合法的数据
* 不要写空的 `except:`，具体类型放在宽泛类型前面

下一节学习 [随机数](rand.md)。用 `python examples/error_demo.py` 运行本节的例子。
