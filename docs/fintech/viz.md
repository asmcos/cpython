# 可视化与时间序列

图是给自己看对不对的。价格跳空、日期乱序、收益率算反了，画出来一眼能发现。

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

简单收益率：今天相对昨天涨了多少。对数收益率以后做研究再用，入门先把 `pct_change` 用对。

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
