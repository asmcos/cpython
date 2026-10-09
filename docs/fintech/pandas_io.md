# 读表、筛选和清洗

上一章的表是手写的。真正上课用的是文件。本章读取教材自带的 `examples/fintech/prices.csv`，查看类型，按条件留下若干行，并处理空值和重复日期。

学完后，应能读入这份 CSV，找出收盘价最高的那一天，并说明清洗时删了什么、填了什么。

## 文件里有什么

`prices.csv` 共十个交易日，列是 `date,open,high,low,close,volume`。日期从 2024-01-02 到 2024-01-15，中间没有周末。收盘价从 10.10 到 11.10。这是课堂用的短样本，用来把读表跑通。作业里的行情应不少于 60 个交易日。

## 读入并排序

在 `examples/fintech/` 目录下运行，或在程序里用文件所在的目录定位 CSV：

```python
from pathlib import Path

import pandas as pd

csv_path = Path(__file__).with_name("prices.csv")
df = pd.read_csv(csv_path, parse_dates=["date"])
print(df.head(3))
print(df.dtypes)
print(len(df))
```

`parse_dates=["date"]` 在读入时就把日期列转成时间，不必再调用一次 `to_datetime`。`head(3)` 只看前三行：

```
        date  open  high   low  close   volume
0 2024-01-02  10.0  10.2   9.9   10.1  1200000
1 2024-01-03  10.1  10.4  10.0   10.3  1500000
2 2024-01-04  10.3  10.5  10.1   10.2  1100000
```

类型：

```
date      datetime64[ns]
open             float64
high             float64
low              float64
close            float64
volume             int64
```

行数是 10。读完先看这三样：前几行、每列类型、一共多少行。列名和预期不一致时，先改读取，再做计算。

按日期排好，后面的收益率才是“后一天比前一天”：

```python
df = df.sort_values("date")
```

这份文件本身已经按日期递增。自己下载的数据不一定，所以排序写在读入之后，成为固定动作。

## 按条件筛选

```python
high = df[df["close"] >= 10.8]
print(high[["date", "close"]])
```

```
        date  close
6 2024-01-10  10.90
7 2024-01-11  10.80
8 2024-01-12  10.95
9 2024-01-15  11.10
```

`df["close"] >= 10.8` 得到一列真假值，再放回 `df[...]`，留下为真的那些行。收盘价不低于 10.8 的有四天。

最高收盘价在哪一天：

```python
best = df.loc[df["close"].idxmax()]
print(best["date"].date(), best["close"])
```

```
2024-01-15 11.1
```

`idxmax()` 给出最大值所在的行标签，`loc` 取出那一行。

## 空值、文字和重复日期

导出的表里，价格有时是文字 `"10.10"`，成交量有时是空的，同一天也可能出现两行。下面用一张小表把这三件事做完。真实文件若已经是数字，就不必强行改类型。

```python
raw = pd.DataFrame(
    {
        "date": ["2024-01-02", "2024-01-02", "2024-01-03"],
        "close": ["10.10", "10.10", None],
        "volume": ["100", None, "80"],
    }
)
print(raw["close"].dtype)
raw["close"] = pd.to_numeric(raw["close"])
raw["volume"] = pd.to_numeric(raw["volume"]).fillna(0)
raw = raw.dropna(subset=["close"])
raw = raw.drop_duplicates(subset=["date"])
print(raw)
```

`close` 一开始的类型是 `object`，因为里面是字符串和空值。`to_numeric` 把它变成数字，无法转换的位置变成 `NaN`。成交量的空值这里填 0，表示“按没有成交记录处理”。收盘价的空值不能填 0：价格为 0 会让收益率失去意义，所以 `dropna(subset=["close"])` 删掉没有收盘价的那一行。`drop_duplicates(subset=["date"])` 保留每个日期的第一行。

清洗之后只剩一行：

```
         date  close  volume
0  2024-01-02   10.1   100.0
```

2024-01-02 的重复行被去掉，2024-01-03 因为没有收盘价被去掉。成交量的空值在被删掉之前已经填成 0，但那一行随后因为收盘价缺失而整行删除，所以最终表里看不到它。

每次清洗都要能回答：删掉了多少行，空值填的是什么。作业里写一句即可。

## Excel

若文件是 `.xlsx`：

```python
df = pd.read_excel("prices.xlsx", sheet_name=0)
```

需要 `python -m pip install openpyxl`。课程作业仍以 CSV 为主，Excel 只作为同一套列被另存时的读法。

## 课堂练习

1. 读入 `prices.csv`，打印列名、行数和 `dtypes`。
2. 找出收盘价最低的那一天。
3. 留下 `volume` 大于 1500000 的行，写出这些日期。

例子见 `examples/fintech/pandas_io.py`。
