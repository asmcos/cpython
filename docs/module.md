#模块

>模块就是已经写好的部分代码，你可以引用

系统也内置了一些写好的模块。

例如：

```
import os
import sys
import time
```

上面三句就是分别引入了三个模块，你可以随便引用其中某一个模块。
os，就是和操作系统相关的 命令。 打开文件，执行文件，切换目录，修改文件名 等都可以。

sys，可以获取程序的执行参数，python版本号，python加载库的路径

time，是和时间相关的。例如：time.time() 获取的就是秒数。time.sleep(1),等待1秒。

使用方法：
------------------

```
print(time.time())

print(sys.version)

print(os.uname())

time.sleep(1)

print(time.time())
```

例子中很多我都是显示了模块的函数执行结果。 实际开发中，并不是用来显示的，而是计算。

更多的引用方法
-----------

```
from sys import version

print (version)

from os import uname

print(uname())

```


#自建一个模块

```
#coding:utf-8

""" 这是一个自己写的 module demo """

website = "http://www.cpython.org"

def help ():
    print("*" * 10)

    print("cpython.org是一个入门文档网站 %s" % website)

    print("*" * 10)
    print(" ")
```

我把上面的代码独立命名了cpython.py 你可以到cpython/examples 目录下寻找

```
https://github.com/asmcos/cpython/tree/master/examples
```

#引用自己建立的模块

```
import cpython

print(cpython.website)
cpython.help()

```

cpython模块有一个变量和一个函数可以被引用。 例子见代码。
