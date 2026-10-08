# 可视化与时间序列

行情文件有了，先画出来核对。价格跳空、日期乱了、收益算反了，图上都能看见。这一章学习收盘价、成交量、简单收益、对数收益，以及 5 日和 20 日均线。

学完后，应能交出一张横轴为日期的价格图，上面叠着两条均线。

## 要会什么

* 画收盘价曲线
* 画成交量
* 算简单收益率和滚动均线
* 把图保存成文件，写进作业

## 价格曲线

```
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/prices.csv", parse_dates=["date"])
df = df.sort_values("date")

plt.figure()
plt.plot(df["date"], df["close"], label="close")
plt.title("Close Price")
plt.xlabel("date")
plt.ylabel("price")
plt.legend()
plt.tight_layout()
plt.savefig("close.png")
```

课堂用默认样式即可。先保证横轴是日期、纵轴是价格。

## 收益率

```
df["ret"] = df["close"].pct_change()
print(df["ret"].describe())
```

简单收益率：今天相对昨天涨了多少。`pct_change()` 就是 `(今收 / 昨收) - 1`。

对数收益率是价格对数的差，多期可以直接相加：

```
import numpy as np

df["log_ret"] = np.log(df["close"]).diff()
```

同一天里，价格变化不大时，两个数很接近。后面做波动率和蒙特卡洛时用对数收益，做净值曲线时用简单收益。先排序，再算这两种收益。

## 均线

```
df["ma5"] = df["close"].rolling(5).mean()
df["ma20"] = df["close"].rolling(20).mean()
```

`rolling(5)` 是最近 5 个交易日。前几天不够窗口，结果是空值，这是正常的。

```
plt.figure()
plt.plot(df["date"], df["close"], label="close")
plt.plot(df["date"], df["ma5"], label="ma5")
plt.plot(df["date"], df["ma20"], label="ma20")
plt.legend()
plt.tight_layout()
plt.savefig("ma.png")
```

## 时间序列注意点

* 先排序，再算 `pct_change` 和 `rolling`
* 停牌、节假日会造成日期不连续，不要用日历日硬减
* 两只股票要比的时候，用日期对齐，不要按行号对齐

## 课堂练习

1. 画出至少 60 个交易日的收盘价。
2. 叠加 5 日、20 日均线。
3. 另存一张收益率直方图：`df["ret"].hist()`。
