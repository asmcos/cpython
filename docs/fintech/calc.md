# 金融计算

把公司金融课上的公式写成函数。先手算一道题，再让程序对答案。

## 要会什么

* 复利终值、现值
* 普通年金
* NPV
* IRR 的含义，以及如何用库函数求解

例子见 `examples/fintech/compound.py`。

## 复利

本金 `pv`，年利率 `r`，年数 `n`，一年复利一次：

```
def future_value(pv, r, n):
    return pv * (1 + r) ** n


print(future_value(10000, 0.05, 3))
```

10000 元、年利率 5%、3 年，终值是 `11576.25`。

现值是反过来：

```
def present_value(fv, r, n):
    return fv / (1 + r) ** n
```

## 普通年金终值

每年末存 `pmt`，利率 `r`，共 `n` 年：

```
def annuity_fv(pmt, r, n):
    return pmt * ((1 + r) ** n - 1) / r
```

## NPV

一组现金流，第 0 期通常是投入（负数）：

```
def npv(rate, cashflows):
    total = 0.0
    for t, cf in enumerate(cashflows):
        total += cf / (1 + rate) ** t
    return total


print(npv(0.1, [-1000, 400, 400, 400]))
```

贴现率 10%，投入 1000，后三年每年收回 400。自己先算，再对程序。

NumPy 也提供 `np.npv` 的历史接口；3.12 环境里更稳妥的是自己按定义写，或使用 `numpy_financial`。课堂以「按定义循环或向量化」为准，避免版本差异。

## IRR

IRR 是让 NPV 等于 0 的贴现率。入门理解含义即可：

```
import numpy as np


def irr(cashflows, guess=0.1):
    rates = np.linspace(-0.9, 2.0, 3000)
    values = [npv(r, cashflows) for r in rates]
    idx = int(np.argmin(np.abs(values)))
    return rates[idx]


print(irr([-1000, 400, 400, 400]))
```

上面是教学用的粗算，不是工业级求解器。作业里写清「近似值」即可。

## 课堂练习

1. 手算：6000 元，年利率 6%，4 年后多少钱？用 `future_value` 验证。
2. 一个项目：年初投入 20000，之后三年每年收回 8000，贴现率 8%，求 NPV。
3. 把函数放到自己的 `finance.py` 模块里，从其他脚本 `import`。
