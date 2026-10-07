# 调试

程序和你想的不一样时，先不要大段重写。按下面顺序查，多数问题都能定位。

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

详细的报错类型和 `try` / `except` 见 [错误和异常](error_except.md)。

## 2. 打印中间结果

在可疑的地方加上 `print`：

```
price = 10
qty = 3
amount = price * qty
print("amount =", amount)
```

金融计算尤其要打印中间量：价格、数量、收益率，确认每一步的数字。例如：

```
price = 10
qty = 3
tax = 0.1
amount = price * qty
print("price =", price, "qty =", qty, "tax =", tax)
total = amount * (1 + tax)
print("total =", total)
```

```
price = 10 qty = 3 tax = 0.1
total = 33.0
```

把每一步算出来的数打出来，一眼就能看出是哪一步算错。

## 3. 用交互环境试一句

在命令行输入 `python` 进入交互环境，把出问题的那一行单独跑一遍。

```
>>> int("56fdsa7")
```

看它到底接受什么样的输入。

## 4. 缩小范围

把程序注释掉一半，看错误还在不在。能复现的最小例子，最容易改。

```
def calc_total(prices):
    total = 0.0
    for p in prices:
        total = total + p   # 先把乘以税率的步骤注释掉
    return total
```

确认循环本身没问题后，再一层层把被注释的部分加回来。

## 5. 用 assert 检查前提

`assert 条件, "说明"` 在条件不成立时抛错，用来检查"这里应该满足的条件"。

```
def positive(n):
    assert n > 0, "n 必须为正数"
    return n
```

`positive(-1)` 会报：

```
AssertionError: n 必须为正数
```

在函数的开头用 `assert` 检查输入是否合法，比运行到一半才发现错误更好定位。

## 6. 官方调试器（选学）

```
python -m pdb examples/hello.py
```

`n` 下一行，`p 变量名` 查看变量，`q` 退出。入门阶段用 `print` 就够，需要单步看程序走到哪时再用 `pdb`。

## 7. 用 logging 而不是 print（进阶）

程序变大后，`print` 打印的东西会混在结果里，还不好关。`logging` 可以把调试信息写到标准错误或文件，还能分级控制。

```
import logging

logging.basicConfig(level=logging.INFO)
logging.debug("只在 debug 级别显示")
logging.info("正常信息")
logging.warning("警告")
```

默认显示 `INFO` 及以上，`debug` 那行不会出现。把 `level=logging.DEBUG` 才能看到。

入门阶段用 `print` 就够；等程序有几十行以上、要长期跑时，再考虑 `logging`。

## 金融场景：核对每一步计算

算复利时，最稳妥的办法是打印中间量，确认每一步数字都对：

```
def future_value(pv, r, n):
    print("pv =", pv, "r =", r, "n =", n)
    step = 1 + r
    print("step =", step)
    result = pv * step ** n
    print("result =", result)
    return result


print(future_value(10000, 0.05, 3))
```

```
pv = 10000 r = 0.05 n = 3
step = 1.05
result = 11576.25
```

调通之后，把中间的 `print` 删掉，只保留返回值，代码就干净了。

## 小结

* 报错从最后一行读起：类型、说明、行号和 `^^^^` 指着的代码
* 在可疑处打印中间结果，金融计算尤其要打印每一步的数字
* 用交互环境单独试出错的那一行
* 注释掉一半代码缩小范围，找到能复现的最小例子
* `assert` 在函数开头检查前提
* 想单步调试用 `pdb`；程序变大后用 `logging` 代替 `print`
* 调通后记得删掉临时 `print`

第一部分到这里结束。接下来进入 [金融科技学习大纲](fintech/index.md)。
