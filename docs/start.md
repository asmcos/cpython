# 开始

例子按 Python 3.12 编写，Windows、macOS、Linux 都可以运行。

先给自己准备一个学习目录，再创建 `hello.py`。目录怎么建、文件怎么建、用什么编辑器，见 [附录一：学习目录和测试代码环境](part1/appendix1.md)。

教材仓库里也有一份现成例子：

* https://github.com/asmcos/cpython/tree/master/examples

## hello.py

在 `python-lab` 目录里创建一个名为 `hello.py` 的文件。

* macOS / Linux：终端里进入目录后，可以用 `touch hello.py` 先建空文件，再用编辑器打开写入。
* Windows PowerShell：可以用 `New-Item hello.py`。
* 三端都可以直接在 IDLE、VS Code 或 Cursor 里 **File → New File**，保存成 `hello.py`。这是最省事的做法。

内容是先打印一句话。

```
print("Hello, World!")
```

Python 3 默认使用 UTF-8，可以直接写中文：

```
print("你好，jeapedu.com")
```

### 运行

先进入你保存 `hello.py` 的目录（附录一里的 `python-lab`），再执行：

```
python3 hello.py
```

Windows 一般写成：

```
python hello.py
```

如果克隆了本教材仓库，也可以在仓库根目录运行现成例子：

```
python3 examples/hello.py
```

如果系统里 `python` 指向的不是 3.12，请用 `python3`。

### 运行结果

```
Hello, World!
你好，jeapedu.com
```

看到这两行，说明环境已经可用。下一节学习 [变量](variables.md)。
