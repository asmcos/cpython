# 分组汇总

读进来的是逐日行情。报表经常要回答另一个问题：这个月一共成交了多少，月末收盘价是多少。本章按月分组，并把结果写回一个新的 CSV。

学完后，应能对 `prices.csv` 做出一张月度表，其中有成交量合计、月末收盘价和交易日天数，并保存为文件。

## 先准备收益率和月份

```python
from pathlib import Path

import pandas as pd

csv_path = Path(__file__).with_name("prices.csv")
df = pd.read_csv(csv_path, parse_dates=["date"]).sort_values("date")
df["ret"] = df["close"].pct_change()
df["month"] = df["date"].dt.to_period("M")
```

`to_period("M")` 把日期收成月份，`2024-01-02` 和 `2024-01-15` 都落在 `2024-01`。周分组把 `"M"` 换成 `"W"`。

## 一次汇总多列

```python
monthly = df.groupby("month", as_index=False).agg(
    volume=("volume", "sum"),
    close_last=("close", "last"),
    days=("close", "size"),
)
print(monthly)
```

```
     month    volume  close_last  days
0  2024-01  13850000        11.1    10
```

`groupby("month")` 把同一个月的行放在一起。`as_index=False` 让月份留在普通列里，方便再写回 CSV。

`agg` 里每一项是“新列名 = (原来的列, 算法)”：

| 新列 | 算法 | 含义 |
| --- | --- | --- |
| `volume` | `sum` | 当月成交量相加 |
| `close_last` | `last` | 组里最后一行的收盘价。日期已经排过序，所以是月末收盘价 |
| `days` | `size` | 这一组有多少行，也就是多少个交易日 |

这份样本只有 2024 年 1 月，所以月度表只有一行。成交量合计 13850000，月末收盘价 11.1，交易日 10 天。

只汇总一列时可以写得更短：

```python
df.groupby("month", as_index=False)["volume"].sum()
```

多列、多种算法时用 `agg`，读起来清楚。

## 写回文件

```python
out = Path(__file__).with_name("monthly_volume.csv")
monthly.to_csv(out, index=False)
```

`index=False` 不把 0、1、2 这种行号写进文件。打开 `monthly_volume.csv`，应能看到表头 `month,volume,close_last,days`。这个文件是计算结果，可以随时删掉再生成。

## 和 describe 的差别

`df.describe()` 对每一列给出计数、均值、标准差、最小、最大等，用来检查有没有明显不合理的数，例如收盘价出现负数。它不按月份切开。要回答“每个月怎样”，用 `groupby`。

## 课堂练习

1. 按月汇总，并核对手工把十天成交量相加是否等于 13850000。
2. 把 `last` 改成 `mean`，列名改成 `close_mean`，比较它和 11.1 哪个更大。
3. 把月度表写到 CSV，再用 `read_csv` 读回来，打印行数。

例子见 `examples/fintech/pandas_group.py`。
