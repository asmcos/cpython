# 调试

程序和你想的不一样时，先不要大段重写。按下面顺序查。

## 1. 把报错读完

Python 3.12 的报错通常会指出文件、行号和出错类型。例如：

```
Traceback (most recent call last):
  File "examples/if.py", line 8, in <module>
    c = b
NameError: name 'b' is not defined
```

先看最后一行：什么错。再看上面：哪一行。

常见类型：

* `NameError`：名字还没定义
* `TypeError`：类型不能这样用
* `ValueError`：值不对
* `IndexError` / `KeyError`：下标或 key 不存在
* `FileNotFoundError`：文件找不到
* `IndentationError`：缩进不对

## 2. 打印中间结果

在可疑的地方加上 `print`：

```
price = 10
qty = 3
amount = price * qty
print("amount =", amount)
```

金融计算尤其要打印中间量：价格、数量、收益率，确认每一步的数字。

## 3. 用交互环境试一句

在命令行输入 `python` 进入交互环境，把出问题的那一行单独跑一遍。

```
>>> int("56fdsa7")
```

看它到底接受什么样的输入。

## 4. 缩小范围

把程序注释掉一半，看错误还在不在。能复现的最小例子，最容易改。

## 5. 官方调试器（选学）

```
python -m pdb examples/hello.py
```

`n` 下一行，`p 变量名` 查看变量，`q` 退出。入门阶段用 `print` 就够。

第一部分到这里结束。接下来进入 [金融科技学习大纲](fintech/index.md)。
