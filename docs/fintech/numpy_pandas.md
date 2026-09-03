# 数据处理：NumPy 和 Pandas

金融数据几乎都是「一张表」：日期、价格、收益率、持仓。这一模块先把表算对。

## 要会什么

* 用 NumPy 数组做向量计算
* 用 Pandas 读 CSV，选列，筛行
* 处理空值，按某一列分组汇总
* 把计算结果写回文件

## NumPy：不要先写循环

```
import numpy as np

prices = np.array([10.0, 10.5, 10.2, 11.0])
returns = prices[1:] / prices[:-1] - 1
print(returns)
print(returns.mean(), returns.std(ddof=1))
```

`prices[1:] / prices[:-1] - 1` 就是相邻两天的简单收益率。金融里很多公式都可以先写成数组运算。

## Pandas：一张行情表

```
import pandas as pd

df = pd.DataFrame(
    {
        "date": ["2024-01-02", "2024-01-03", "2024-01-04"],
        "close": [10.0, 10.5, 10.2],
        "volume": [1000, 1200, 800],
    }
)
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")
print(df)
print(df["close"].pct_change())
```

`pct_change()` 是简单收益率。日期建议变成时间类型，并设为索引，后面画图、对齐多只股票都方便。

## 读本地文件

```
df = pd.read_csv("data/prices.csv", parse_dates=["date"])
df = df.sort_values("date")
print(df.head())
print(df.describe())
```

Excel：

```
df = pd.read_excel("data/prices.xlsx", sheet_name=0)
```

需要先安装 `openpyxl`。

## 清洗

```
df = df.dropna(subset=["close"])
df = df.drop_duplicates(subset=["date"])
df["close"] = df["close"].astype(float)
```

真实数据常有空行、重复日期、把价格存成了字符串。先检查再计算。

## 分组

```
df["month"] = df["date"].dt.to_period("M")
monthly = df.groupby("month", as_index=False)["volume"].sum()
print(monthly)
```

按月汇总成交量，是后面做报表的基本动作。

## 课堂练习

1. 自己造 10 天收盘价，用 NumPy 算收益率均值。
2. 读一份 CSV，找出收盘价最高的那一天。
3. 把缺失的 `volume` 填成 0，再按周汇总。

例子见 `examples/fintech/returns.py`。
