# 金融数据获取

读表和收益率在 [用数组算收益率](numpy_returns.md) 和 [读表、筛选和清洗](pandas_io.md) 里已经练过。这一章学习准备自己的日行情：认清开高低收，用本地文件把读取跑通，再把新下载的结果存成 CSV。后面的画图和计算都读这份文件。

学完后，应能交出至少 60 个交易日，并写明数据来源和是否复权。

1. 认字段：日期、开高低收、成交量，并记下是否复权。
2. 用本地 CSV 完成读取、排序和类型转换。样本文件是 `examples/fintech/prices.csv`。
3. 下载新行情后立刻存成 CSV。画图和计算都读这个文件。

日 K 的下载示例在 [quantrader](https://github.com/asmcos/quantrader) 的 `01-股票的数据获取`。把其中一种日 K 结果保存下来即可。作业提交保存后的文件，并写明数据来源和复权口径。

## 要会什么

* 看懂日行情常用字段
* 把日期解析对，并按时间排序
* 把接口或网页下来的 JSON 收成 DataFrame
* 写清数据来源、频率、复权与否

## 日行情常见字段

| 字段 | 含义 |
| --- | --- |
| date | 交易日 |
| open | 开盘价 |
| high | 最高价 |
| low | 最低价 |
| close | 收盘价 |
| volume | 成交量 |

还可以有复权收盘价、成交额、股票代码。作业里必须注明：这是前复权、后复权，还是不复权。不同口径不能混着算收益。

## 最小可用的本地 CSV

```
date,open,high,low,close,volume
2024-01-02,10.00,10.20,9.90,10.10,1200000
2024-01-03,10.10,10.40,10.00,10.30,1500000
```

```
import pandas as pd

df = pd.read_csv("data/prices.csv", parse_dates=["date"])
df = df.sort_values("date").reset_index(drop=True)
print(df.dtypes)
print(df.tail())
```

## 从字典列表构造

接口返回常常是 JSON 数组。先看成 Python 的 `list[dict]`：

```
rows = [
    {"date": "2024-01-02", "close": 10.1},
    {"date": "2024-01-03", "close": 10.3},
]
df = pd.DataFrame(rows)
df["date"] = pd.to_datetime(df["date"])
```

## 保存一份，避免反复下载

```
df.to_csv("data/prices_clean.csv", index=False)
```

研究脚本应该能在断网时跑通。下载是一回事，计算是另一回事。

## 使用外部数据时的纪律

1. 遵守数据源的使用条款，不把密钥写进公开仓库。
2. 记录下载日期和代码版本。
3. 作业提交时附带数据文件，或附带「如何获得这份数据」的说明。
4. 不要把实时行情作业建立在随时会失效的网页结构上。

网络请求写法见 [网络接口](api.md)。
