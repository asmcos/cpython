# 收益分布与风险价值

价格和均线已经画过。这一章看过去的日收益本身：平均每天波动多大，较差的那 5% 差到什么程度，以及按这个波动模拟一年，价格会落在哪里。

学完后，应能在自己的行情上写出日波动率、年化波动率和 95% 历史模拟风险价值，并注明样本有多少个交易日。例子见 `examples/fintech/risk_demo.py`。

## 从收盘价到对数收益

```
import numpy as np
import pandas as pd

df = pd.read_csv("data/prices.csv", parse_dates=["date"])
df = df.sort_values("date")
df["ret"] = df["close"].pct_change()
df["log_ret"] = np.log(df["close"]).diff()
log_ret = df["log_ret"].dropna()
```

`ret` 是简单收益，用来连乘净值。`log_ret` 是对数收益，多天的对数收益相加，等于整段价格的对数变化。

看分布时先打描述统计：

```
print(log_ret.describe())
print("mean =", log_ret.mean())
print("std  =", log_ret.std(ddof=1))
```

均值是这段样本里平均每天涨多少（对数）。标准差就是这段样本的日波动率。交易日大约 252 天，年化波动率常写成：

```
ann_vol = log_ret.std(ddof=1) * np.sqrt(252)
print("ann_vol =", ann_vol)
```

作业里写明：这是样本标准差，并且假设每天独立。

## 95% 历史模拟风险价值

历史模拟不用先假设收益服从正态分布。把过去的日收益从小到大排好，取最差的那 5% 的分界。

```
q = log_ret.quantile(0.05)
var_95 = -q
print("5% quantile =", q)
print("95% historical VaR =", var_95)
```

若 `q` 是 `-0.02`，表示样本里约有 5% 的交易日，对数收益差于 `-2%`。`var_95` 把这个数写成正的损失幅度：`0.02`。

这是样本里的分位数，不是对明天的保证。样本只有几十天时，5% 分位数只有两三天在支撑，数字会跳。作业至少用 60 个交易日，并写上「95%、日频、对数收益、历史模拟」。

简单收益也可以做同一件事，两种口径不要混在一个句子里。

## 一次蒙特卡洛

假设今后每个交易日的对数收益相互独立，并且来自同一个正态分布，均值和标准差用历史样本估计：

```
rng = np.random.default_rng(7)
mu = log_ret.mean()
sigma = log_ret.std(ddof=1)

drawn = rng.normal(mu, sigma, size=252)
price0 = df["close"].iloc[-1]
path = price0 * np.exp(np.cumsum(drawn))
print("start =", price0)
print("end   =", path[-1])
```

`252` 是一年的交易日。`cumsum` 把每天的对数收益加起来，`exp` 变回价格。`default_rng(7)` 固定随机序列，同一份代码每次运行得到同一条路径，报告才能复现。

多画几条，才看得出范围：

```
ends = []
for i in range(500):
    drawn = rng.normal(mu, sigma, size=252)
    end = price0 * np.exp(np.cumsum(drawn)[-1])
    ends.append(end)

ends = np.array(ends)
print("median end =", np.median(ends))
print("5% end     =", np.quantile(ends, 0.05))
```

500 次里，期末价格的 5% 分位数是这套假设下较差的那一档年末价格。它和历史模拟风险价值不是同一个数：一个看过去真实出现过的日收益，一个看正态假设下模拟出来的一年。

样本只有十来天、而且整体在涨时，日均收益会被抬得很高，模拟一年后的价格会离起点很远。作业改用至少 60 个交易日再解释结果。

报告里写三句就够：均值和波动率从哪段历史来，模拟了多少条、多少天，正态和独立是假设。

## 课堂练习

1. 在自己的 60 日行情上算出对数收益的均值、日波动率和年化波动率。
2. 写出 95% 历史模拟风险价值，并说明样本有多少天。
3. 用同一个随机种子模拟 500 条一年路径，报告期末价格的中位数和 5% 分位数。
