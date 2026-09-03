# 金融数据获取

先把本地文件用熟，再碰网络接口。课堂和作业默认以本地 CSV 为准，这样结果可复现。

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

仓库里有一份演示数据：`examples/fintech/prices.csv`。作业可以先用它，再换成自己的数据。

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
