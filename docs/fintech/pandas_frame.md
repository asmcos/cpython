# Series 与 DataFrame

`Series` 是一列数据。`DataFrame` 由多个 `Series` 并排组成，这些列共用同一套行号，于是成为一张表。行情里的日期、收盘价、成交量各是一列；放进同一张表之后，同一行就是同一天。

从这张表里取出一列，得到的仍是 `Series`。本章用它计算简单收益率，并按行号和标签取得其中某一个数。

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

## DataFrame：多列并排

把日期、收盘价、成交量各做成一列，再并排放进一张表：

```python
date = pd.Series(["2024-01-02", "2024-01-03", "2024-01-04"], name="date")
volume = pd.Series([1000, 1200, 800], name="volume")
df = pd.DataFrame({"date": date, "close": close, "volume": volume})
print(df)
print(type(df["close"]).__name__)
```

```
         date  close  volume
0  2024-01-02   10.0    1000
1  2024-01-03   10.5    1200
2  2024-01-04   10.2     800
Series
```

三列长度相同，第 0 行就是 2024-01-02、价格 10.0、成交量 1000。`df["close"]` 把收盘价这一列取回来，类型仍是 `Series`，数值也仍是 10.0、10.5、10.2。

每一列保持自己的类型：日期是字符串，收盘价是小数，成交量是整数。日期和价格不要塞进同一个 `Series`，否则这一列无法再按数字计算。

## 建表的其他写法

上面是先有 `Series`，再拼成表。同一张表还可以直接写出来。下面三种写法的打印结果，和上一节那张表相同。

按列写。字典的键是列名，值是这一列的数据。手写一小段行情时，这样最直接。

```python
df = pd.DataFrame(
    {
        "date": ["2024-01-02", "2024-01-03", "2024-01-04"],
        "close": [10.0, 10.5, 10.2],
        "volume": [1000, 1200, 800],
    }
)
```

按行写。列表里的每一项是一天，键仍然是列名。记录是一条一条到来时，适合这种写法。

```python
df = pd.DataFrame(
    [
        {"date": "2024-01-02", "close": 10.0, "volume": 1000},
        {"date": "2024-01-03", "close": 10.5, "volume": 1200},
        {"date": "2024-01-04", "close": 10.2, "volume": 800},
    ]
)
```

先写行，再另给列名。每一行是一个列表，顺序必须和 `columns` 一致。

```python
rows = [
    ["2024-01-02", 10.0, 1000],
    ["2024-01-03", 10.5, 1200],
    ["2024-01-04", 10.2, 800],
]
df = pd.DataFrame(rows, columns=["date", "close", "volume"])
```

已经有 NumPy 数组时，也可以直接交给 `DataFrame`。数组里的数会变成同一种类型，所以这里的成交量也成了小数：

```python
import numpy as np

arr = np.array([[10.0, 1000], [10.5, 1200], [10.2, 800]])
df = pd.DataFrame(arr, columns=["close", "volume"])
print(df)
```

```
   close  volume
0   10.0  1000.0
1   10.5  1200.0
2   10.2   800.0
```

日期和价格类型不同，不要放进同一个数组再转成表。那种行情用前面的字典即可。从 CSV 读入一整张表，放到下一章。

## 取一列和取若干列

取出一列，得到 `Series`。取出若干列，得到的仍是由这些列组成的 `DataFrame`。

```python
close = df["close"]
print(type(close).__name__)
print(close)

part = df[["date", "close"]]
print(type(part).__name__)
print(part.shape)

only = df[["close"]]
print(type(only).__name__)
print(only.shape)
```

```
Series
0    10.0
1    10.5
2    10.2
Name: close, dtype: float64
DataFrame
(3, 2)
DataFrame
(3, 1)
```

`df["close"]` 是一对中括号，取出这一列，结果是 `Series`。后面的 `pct_change()`、`mean()` 都写在这一列上。

`df[["date", "close"]]` 是中括号里再放一个列名列表，留下两列，结果仍是 `DataFrame`，形状是 3 行 2 列。

`df[["close"]]` 看起来也只取了收盘价，但因为外面还有一层列表，结果是 3 行 1 列的 `DataFrame`。需要把这一列继续和其他表拼接、或保持表的写法时，用这种形式。只想对价格做计算时，用 `df["close"]`。

列名写错会得到 `KeyError`。先打印 `df.columns`，核对拼写。

## 计算落在一列上，还是落在整张表上

```python
print(close.mean())
print(df[["close", "volume"]].mean())
```

```
10.233333333333333
close       10.233333
volume    1000.000000
dtype: float64
```

`Series.mean()` 把这一列收成一个数。`DataFrame.mean()` 对每个数值列各算一个均值，返回的是一个新的 `Series`：索引是列名，值是该列的均值。成交量的均值是 1000，因为 `(1000 + 1200 + 800) / 3 = 1000`。

因此，收益率、波动率这类针对价格的计算，先取出 `Series` 再算。想同时看收盘价和成交量时，先选出这两列，再对这张小表调用 `mean()`。日期列是字符串或时间，直接对整张表求均值会失败，所以不要把它放进这次计算。

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

`iloc` 按下标，从 0 数。`iloc[0]` 取出表里的第一行。一行横过来也是一个 `Series`，索引变成了列名：

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

1. 用两个 `Series` 做成一张只有 `date` 和 `close` 的表，至少四行。再用「按列的字典」写一张同样的表，并确认两张表的收盘价一致。
2. 对 `close` 这一列和整张表的数值列分别求均值，说明两个结果的类型。
3. 打印 `pct_change()`，用 `iloc` 取出最后一行，用 `loc` 取出某一行的收盘价。
4. 打印 `dtypes`，确认日期列已经是时间类型。

例子见 `examples/fintech/pandas_frame.py`。
