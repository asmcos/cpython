# Series 与 DataFrame

NumPy 适合一列纯数字。行情文件里还有日期、成交量，后面还会添上收益率。Pandas 用 `Series` 表示一列，用 `DataFrame` 表示一整张表。

学完后，应能自己做出一张含日期、收盘价、成交量的表，取出一列或几列，按行号和标签取到某一个数，并给表增加收益率列。

## 安装

```
python -m pip install pandas
```

## Series：带名字的一列

```python
import pandas as pd

close = pd.Series([10.0, 10.5, 10.2], name="close")
print(close)
print(close.mean())
```

```
0    10.0
1    10.5
2    10.2
Name: close, dtype: float64
10.233333333333333
```

左边的 0、1、2 是索引，右边是值。`name` 是列名。均值约 10.2333，和 `(10 + 10.5 + 10.2) / 3` 相同。

## DataFrame：一张表

```python
df = pd.DataFrame(
    {
        "date": ["2024-01-02", "2024-01-03", "2024-01-04"],
        "close": [10.0, 10.5, 10.2],
        "volume": [1000, 1200, 800],
    }
)
print(df)
```

```
         date  close  volume
0  2024-01-02   10.0    1000
1  2024-01-03   10.5    1200
2  2024-01-04   10.2     800
```

字典的每个键是一列的名字，每个值是这一列的数据。三列长度必须相同，否则建表会失败。

## 取列

```python
print(df["close"])
print(df[["date", "close"]])
```

一对中括号取一列，得到 `Series`。两对方括号里放一个列名列表，得到仍是表的那几列。列名写错会得到 `KeyError`，先看 `df.columns`。

## 增加一列

```python
df["ret"] = df["close"].pct_change()
print(df)
```

```
         date  close  volume       ret
0  2024-01-02   10.0    1000       NaN
1  2024-01-03   10.5    1200  0.050000
2  2024-01-04   10.2     800 -0.028571
```

`pct_change()` 就是上一章的简单收益率。第一行没有前一天，结果是 `NaN`，表示缺失。后面做均值、画图之前要决定怎么处理它，通常是删掉这一行，而不是把它当成 0。0 表示“没涨没跌”，和“没有前一天”不是同一件事。

## 取行：iloc 和 loc

```python
print(df.iloc[0])
print(df.loc[1, "close"])
```

`iloc` 按下标，从 0 数。`iloc[0]` 是表里的第一行：

```
date      2024-01-02
close           10.0
volume          1000
ret              NaN
Name: 0, dtype: object
```

`loc` 按索引标签和列名。这里行的标签正好也是 0、1、2，所以 `loc[1, "close"]` 是 10.5。等日期被设成索引之后，`loc` 里就要写日期，不能再把行号当成日期。

## 把日期列变成时间

```python
df["date"] = pd.to_datetime(df["date"])
print(df.dtypes)
```

```
date      datetime64[ns]
close            float64
volume             int64
ret              float64
dtype: object
```

`dtypes` 列出每一列的类型。日期变成 `datetime64` 之后，才能按月份、按星期取出部分字段。这一步放在筛选和分组之前做。

## 课堂练习

1. 做一张只有 `date` 和 `close` 的表，至少四行，打印 `pct_change()`。
2. 用 `iloc` 取出最后一行，用 `loc` 取出某一行的收盘价。
3. 打印 `dtypes`，确认日期列已经是时间类型。

例子见 `examples/fintech/pandas_frame.py`。
