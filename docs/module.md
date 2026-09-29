# 模块

一个 `.py` 文件就是一个模块。`import` 把另一个文件里的变量和函数拿过来用。

上一节的 [函数](functions.md) 把重复的代码收进一个名字。文件变多以后，再按用途拆开：算时间的放一起，读写文件的放一起。Python 自己带了一批这样的文件，叫做标准库，装好 Python 就能 `import`，不用另外安装。别人写的第三方库要用 pip 装，见下一节 [安装其他模块](pip.md)。

## 引用标准库

~~~
import os
import sys
import time
~~~

* `os`：和操作系统有关，例如当前目录、文件名
* `sys`：程序参数、Python 版本、模块搜索路径
* `time`：时间戳、延时

模块名后面加一个点，再写里面的函数名：

~~~
print(time.time())
print(sys.version)
print(os.getcwd())
time.sleep(1)
print(time.time())
~~~

`time.time()` 是从 1970 年起到现在的秒数，带小数。中间 `time.sleep(1)` 让程序停 1 秒，所以第二次打印的数大约比第一次大 1。具体数字每次运行都不一样。更完整的时间函数见 [时间](time.md)。

`sys.version` 是当前 Python 的版本说明。`os.getcwd()` 是你敲命令时所在的目录，Windows、macOS、Linux 都能用。

`os.uname()` 只在部分 Unix 系统上有，入门阶段不要用它。

这些函数在真实项目里通常是拿来计算，不一定打印。

`import` 一般写在文件最上面。教材例子为了对着某一节看，有时把 `import` 放在使用它的代码旁边。

## from 和 as

`import sys` 之后，用 `sys.version` 才能读到版本。这里其实有两件可以分开决定的事：

* `from`：拿整个模块，还是只拿里面的某一个名字
* `as`：这个名字在当前文件里叫什么

两件事情可以单用，也可以写在同一行。下面四种写法读到的是同一个版本字符串：

~~~
import sys
print(sys.version)

import sys as system
print(system.version)

from sys import version
print(version)

from sys import version as py_version
print(py_version)
~~~

四次打印的文字一样，都是当前 Python 的版本说明，内容因电脑而异。可以放在一起比：

~~~
print(sys.version == system.version == version == py_version)
~~~

~~~
True
~~~

对照着看，差别只在当前文件里的名字：

| 写法 | 当前文件里怎么用 |
| --- | --- |
| `import sys` | `sys.version`，模块名仍叫 `sys` |
| `import sys as system` | `system.version`，模块换了个称呼 |
| `from sys import version` | 直接写 `version`，不再加 `sys.` |
| `from sys import version as py_version` | 直接写 `py_version` |

`from sys import version` 只把 `version` 这个名字拿进来。如果文件里没有另外写过 `import sys`，就不能再写 `sys.version`，因为 `sys` 这个模块名并没有留在当前文件里。

`as` 换的是当前文件里的称呼，不是模块文件本身。`import sys as system` 之后，标准库里的模块还是叫 `sys`，只是这份代码用 `system` 去点它。

一次拿进多个名字，用逗号隔开，每个名字自己也可以带 `as`：

~~~
from time import time, sleep as pause
print(time())
pause(1)
~~~

`time()` 是时间戳，`pause(1)` 就是 `sleep(1)`，程序停 1 秒。

名字会盖住前面的同名变量。只写 `from time import time` 时，当前文件里的 `time` 变成了函数，不能再把它当模块用：

~~~
from time import time
time.sleep(1)
~~~

~~~
AttributeError: 'builtin_function_or_method' object has no attribute 'sleep'
~~~

要用模块里的好几个函数，就 `import time`，调用时写 `time.time()`、`time.sleep(1)`。或者 `from time import time, sleep`，两个名字分开拿。

`from 模块 import *` 会把模块里的名字一股脑倒进当前文件，看不出哪个名字是谁的，还可能盖住你已经写好的变量。入门不要这样写。

## 自己写一个模块

模块名就是文件名去掉 `.py`。仓库里的 `examples/cpython.py` 就是一个叫 `cpython` 的模块：

~~~
website = "https://jeapedu.com"


def show_site():
    print("*" * 10)
    print(f"jeapedu.com 是一个入门文档网站 {website}")
    print("*" * 10)
    print(" ")


if __name__ == "__main__":
    show_site()
~~~

它有一个变量 `website`，一个函数 `show_site`。函数不要命名成 `help`：那是 Python 自带的帮助函数，同名之后再写 `help()` 就叫不到原来的那个了。

## 引用自己的模块

在 `examples` 目录里，或者在仓库根目录运行 `python examples/module.py`，都可以这样引用旁边的 `cpython.py`：

~~~
import cpython

print(cpython.website)
cpython.show_site()
~~~

~~~
https://jeapedu.com
**********
jeapedu.com 是一个入门文档网站 https://jeapedu.com
**********
~~~

最后的 `print(" ")` 还会再打出一个空格。

`from` 和 `as` 的规则与标准库相同。只要 `website` 这一个变量时写 `from cpython import website`，想给模块换称呼时写 `import cpython as site`，再用 `site.website`。模块已经加载过之后，再写一次 `import` 不会重新执行文件。

## Python 去哪里找模块

`import cpython` 时，Python 按 `sys.path` 这个列表逐个目录找 `cpython.py`。列表的第一项是**当前脚本所在的目录**，不是你敲命令时的工作目录。

~~~
import sys
print(sys.path[0])
~~~

运行 `python examples/module.py` 时，这一项是 `examples` 的绝对路径，所以能找到旁边的 `cpython.py`。后面还有标准库目录，以及用 pip 装进去的第三方库目录。每个人电脑上的完整路径不一样，先看懂第一项即可。

因此有两件容易混的事：

* `os.getcwd()` 是运行命令时的目录。在仓库根目录执行，它就是仓库根目录。
* `sys.path[0]` 是脚本文件自己坐落的目录。脚本在 `examples` 里，第一项就是 `examples`。

自己的文件不要叫 `time.py`、`os.py`、`random.py`。搜索时先看到脚本旁边的同名文件，`import time` 就会找到你的文件，而不是标准库。

## 直接运行和被导入

模块最顶上的代码，在 `import` 时就会执行。定义函数只是把函数记下来，真正的打印、计算如果写在顶层，一导入就会跑。

文件被直接运行时，`__name__` 的值是 `"__main__"`。被别人 `import` 时，`__name__` 是模块名，例如 `"cpython"`。

~~~
if __name__ == "__main__":
    show_site()
~~~

所以：

* `python examples/cpython.py` 会调用 `show_site()`
* `import cpython` 只会拿到 `website` 和 `show_site`，不会自动打印

演示用的调用放进这个 `if` 里。别的文件导入时，就只使用函数，不会把演示再跑一遍。

## 常见坑

**找不到模块。** 文件名和 `import` 后面的名字不一致，或者文件不在 `sys.path` 里，都会报错：

~~~
import no_such_module
~~~

~~~
ModuleNotFoundError: No module named 'no_such_module'
~~~

模块名用文件名，不要带 `.py`。写 `import cpython.py` 是错的。

**文件名挡住了标准库。** 自己的练习不要保存成 `time.py`。要练时间模块，文件可以叫 `time_demo.py`，里面再 `import time`。

**导入时执行了不该执行的代码。** 顶层的 `print`、输入、改文件，在 `import` 时都会发生。只在直接运行时才该做的事，放进 `if __name__ == "__main__":`。

**`from 模块 import *`。** 名字从哪来看不出来，还可能盖住你已经写好的变量。需要谁就导入谁。

## 小结

* 一个 `.py` 文件是一个模块，模块名是去掉后缀的文件名
* `from` 决定拿整个模块还是其中的名字，`as` 决定这个名字在当前文件里叫什么，两者可以写在同一行
* 标准库不用安装。第三方库见 [安装其他模块](pip.md)
* Python 先在脚本所在目录找，再找标准库和已安装的库
* 不要用 `time.py` 这种标准库同名文件
* 直接运行时 `__name__` 是 `"__main__"`，被导入时是模块名

下一节学习 [安装其他模块](pip.md)。用 `python examples/module.py` 运行本节的例子。直接运行模块本身则是 `python examples/cpython.py`。
