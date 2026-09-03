# 附录一：学习目录和测试代码环境

写代码前，先规划好目录，再按步骤操作。还没装 Python 的，先看 [安装 Python 3.12](install.md)。

## 规划目录

本课固定用一个学习目录，不要把 `.py` 文件随便扔在桌面上。

| 系统 | 目录 |
| --- | --- |
| macOS / Linux | `~/python-lab` |
| Windows | `C:\Users\你的用户名\python-lab` |

规划好的结构如下。`hello.py` 是第一课要建的文件，`examples/` 用来放后面每一节的练习。

```
python-lab/
    hello.py
    examples/
```

说明：

* `~` 表示当前用户的主目录。Windows 也可以写成 `%USERPROFILE%\python-lab`。
* 文件名必须是 `hello.py`，不要用 Word，也不要存成 `hello.py.txt`。
* Windows 建议在资源管理器「查看」里勾选「文件扩展名」，避免看不出真实后缀。

编辑器可以选 IDLE（Python 自带）、VS Code 或 Cursor。不要用 Word。

## 操作步骤

按下面顺序做。后面凡是命令，都在终端里输入，不要写进 `.py` 文件。

### 第 1 步：打开终端

* macOS：打开「启动台」→「终端」。也可以按 `Command + 空格`，输入 `Terminal` 回车。
* Windows：开始菜单里搜「PowerShell」或「命令提示符」。建议用 PowerShell。
* Linux：打开系统自带的终端。

打开后，窗口里会有一个闪烁光标，这就是终端。后面第 2 步到第 5 步都在这个窗口里做。

### 第 2 步：创建规划好的目录

macOS / Linux：

```
mkdir -p ~/python-lab/examples
cd ~/python-lab
pwd
```

Windows PowerShell：

```
mkdir $HOME\python-lab\examples
cd $HOME\python-lab
pwd
```

Windows 命令提示符：

```
mkdir %USERPROFILE%\python-lab\examples
cd %USERPROFILE%\python-lab
cd
```

`mkdir` 创建目录，`cd` 进入目录，`pwd`（命令提示符用 `cd`）打印当前路径。看到路径末尾是 `python-lab`，说明这一步完成。

以后每次写代码，也是先打开终端，再 `cd` 进这个目录。

### 第 3 步：创建 hello.py

会一种方法即可。推荐方法 A。

**方法 A：用编辑器新建**

1. 打开 IDLE、VS Code 或 Cursor
2. 菜单 **File → New File**
3. **File → Save**，保存到刚才的 `python-lab` 目录，文件名填 `hello.py`

**方法 B：macOS / Linux 用 touch**

终端要还在 `python-lab` 里（第 2 步的 `cd` 做过）。然后输入：

```
touch hello.py
```

`touch` 只创建空文件，接下来还要用编辑器打开再写内容：

```
code hello.py
```

没有 `code` 命令时，可用 Cursor：`cursor hello.py`。也可以用 `nano hello.py`，写完后 `Ctrl + O` 保存，`Ctrl + X` 退出。

**方法 C：Windows 用 PowerShell**

```
New-Item hello.py
notepad hello.py
```

`New-Item` 可简写成 `ni hello.py`。命令提示符可用 `type nul > hello.py`。记事本保存时编码选 UTF-8。建议尽快换成 VS Code 或 Cursor。

### 第 4 步：写入代码并保存

不管文件是怎么创建的，内容都写成：

```
print("Hello, World!")
print("你好，jeapedu.com")
```

保存后再回到终端运行。先确认终端的当前目录仍是 `python-lab`。

### 第 5 步：在终端里运行

如果刚才去编辑器写代码时关掉了终端，再打开一次终端，并重新进入目录：

```
cd ~/python-lab
```

Windows PowerShell 用：

```
cd $HOME\python-lab
```

确认当前目录和文件：

```
pwd
```

macOS / Linux 用 `ls` 看有没有 `hello.py`，Windows PowerShell 用 `dir`。

然后运行：

```
python3 hello.py
```

Windows 一般写成：

```
python hello.py
```

成功时输出：

```
Hello, World!
你好，jeapedu.com
```

如果提示找不到命令，回到 [安装 Python 3.12](install.md)，检查是否勾选了 **Add python.exe to PATH**。macOS 请用 `python3`。

如果提示找不到文件，多半是还没 `cd` 进 `python-lab`。回到第 1 步打开终端，再做第 2 步的 `cd`。

## 可选：虚拟环境

第一周写 `hello.py` 可以先不用。从 [安装模块（pip / venv）](../pip.md) 开始，在 `python-lab` 里执行：

```
python3 -m venv .venv
```

Windows 把 `python3` 换成 `python`。激活方式见那一节。

搭好环境后，回到 [开始：Hello World](../start.md) 把例子跑通。
