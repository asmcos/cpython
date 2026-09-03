# 模块

模块就是已经写好的代码，你可以引用。Python 自己也带了一批模块。

```
import os
import sys
import time
```

* `os`：和操作系统有关，例如当前目录、文件名
* `sys`：程序参数、Python 版本、模块搜索路径
* `time`：时间戳、延时

## 使用

```
print(time.time())
print(sys.version)
print(os.getcwd())
time.sleep(1)
print(time.time())
```

`os.getcwd()` 在 Windows、macOS、Linux 都能用。`os.uname()` 只在部分 Unix 系统上有，入门阶段不要用它。

这些函数在真实项目里通常是拿来计算，不一定打印。

## 另一种引用写法

```
from sys import version

print(version)
```

`from 模块 import 名字` 之后，可以直接用这个名字，不用再写 `模块.`。

## 自己写一个模块

把下面代码保存为 `examples/cpython.py`：

```
website = "https://jeapedu.com"


def help():
    print("*" * 10)
    print(f"jeapedu.com 是一个入门文档网站 {website}")
    print("*" * 10)
    print(" ")
```

## 引用自己的模块

在同一个目录下：

```
import cpython

print(cpython.website)
cpython.help()
```

这个模块里有一个变量 `website` 和一个函数 `help()`。例子见仓库 `examples/` 目录。
