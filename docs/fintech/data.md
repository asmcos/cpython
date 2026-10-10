# 金融数据获取

前面用教材自带的 `prices.csv` 练习读表和收益率。这一章换成一只真实股票的日 K：向公开行情接口要数据，认清每一列，立刻存成 CSV。后面的画图和计算读这份文件，不再反复请求网络。

这里讲两种日 K。[quantrader](https://github.com/asmcos/quantrader) 的 `01-股票的数据获取` 里还有分时和股票列表，课程作业只要求把日 K 保存下来。两种途径都取前复权，代码写成 `sz000001`、`sh600000` 这种形式：`sz` 是深圳，`sh` 是上海，后面六位是股票代码。

## 日行情要留下哪些列

| 列名 | 含义 |
| --- | --- |
| date | 交易日 |
| open | 开盘价 |
| high | 最高价 |
| low | 最低价 |
| close | 收盘价 |
| volume | 成交量，下面两个例子里的单位都是手 |

作业必须写明三件事：数据来源、频率是日 K、价格是前复权。前复权、后复权和不复权不能混在同一次收益计算里。

先用本地文件把读取跑通。样本是 `examples/fintech/prices.csv`，不需要联网：

```python
import pandas as pd

df = pd.read_csv("prices.csv", parse_dates=["date"])
df = df.sort_values("date").reset_index(drop=True)
print(df.dtypes)
print(df.tail())
```

## 腾讯日 K

腾讯这一条取的是前复权日 K。参数写在查询字符串里：股票代码、`day`、两个留空的日期、根数、`qfq`。`qfq` 就是前复权。根数先写 5，用来看清字段；作业再改成不少于 60。

```python
import json
import re

import requests

code = "sz000001"
url = "https://proxy.finance.qq.com/ifzqgtimg/appstock/app/newfqkline/get"
resp = requests.get(
    url,
    params={"_var": "kline_dayqfq", "param": f"{code},day,,,5,qfq"},
    timeout=15,
)
resp.raise_for_status()
resp.encoding = "utf-8"
```

返回的正文不是纯 JSON。开头有一段变量名：

```
kline_dayqfq={"code":0,"msg":"","data":{"sz000001":{"qfqday":[ ...]}}}
```

先取出大括号里的对象，再解析：

```python
match = re.search(r"kline_dayqfq\s*=\s*({.*})\s*$", resp.text, re.DOTALL)
payload = json.loads(match.group(1))
raw = payload["data"][code]["qfqday"]
print(raw[-1][:6])
```

!!! note "这行正则在找什么"

    `re.search` 在整段返回文字里找第一处符合模式的内容。`r"..."` 是原始字符串，里面的 `\s` 会按正则交给 `re`，而不会被 Python 当成转义。模式从左到右是：

    | 片段 | 含义 |
    | --- | --- |
    | `kline_dayqfq` | 就这三个字，变量名本身 |
    | `\s*` | `\s` 是空白，包括空格、换行和 Tab。`*` 表示这种空白可以出现 0 次或多次。等号两边都写了 `\s*`，所以 `kline_dayqfq={` 和 `kline_dayqfq = {` 都能对上 |
    | `({.*})` | 圆括号是分组，`match.group(1)` 取到的就是这对括号里的内容。`{` 和 `}` 前的反斜杠表示字面量大括号。`.` 是任意字符。`*` 默认是贪婪的：先尽量多吃，再往回吐，直到后面的 `}` 和 `$` 也能对上 |
    | `$` | 锚点，表示必须匹配到字符串结尾。它本身没有贪婪或不贪婪这一说 |
    | `re.DOTALL` | 这是传给 `search` 的标志，不是模式里的字符。默认情况下 `.` 不匹配换行；加上 `DOTALL` 之后，正文被拆成多行时，`.*` 仍能一直读到最后的 `}` |

    `$` 和贪婪是两件事，但写在一起会互相约束。`.*` 若在中途遇见第一个 `}` 就停，后面还剩一大段 JSON，`$` 就对不上结尾。贪婪的 `.*` 会继续吃，再把多吃的字符退回来，退到「最后一个 `}`，并且这个 `}` 之后只剩空白、紧接着就是结尾」为止。所以这里取到的是整段 `{"code":0,...}`，而不是 `qfqday` 里面更早出现的那个 `}`。

    若把 `.*` 写成 `.*?`，量词变成非贪婪，会从最短开始试。因为后面仍有 `$`，第一次停在最早的 `}` 时结尾对不上，它还是得继续加长，最后往往和贪婪写法停在同一处。没有末尾的 `$` 时，两者才分开：贪婪停在最后一个 `}`，非贪婪停在第一个 `}`。

    腾讯这条返回本身就结束在最后的 `}` 上，去掉 `$`，贪婪的 `.*` 仍停在那个 `}`，取到的 JSON 和原来一样。`$` 约束的是后面不许再有别的字。若正文在 `}` 之后还有一句说明，带 `$` 的模式对不上结尾，`search` 得到 `None`；去掉 `$` 则只匹配到最后一个 `}`，后面的说明不进入分组，JSON 仍然可以解析。

    分组里拿到的就是这一整段 JSON，接着交给 `json.loads`。正则的其余符号见 [正则](../re.md)。

最近一根是：

```
['2026-10-09', '11.78', '11.59', '11.89', '11.58', '1078106.00']
```

每一根的前六项依次是日期、开盘、收盘、最高、最低、成交量。收盘排在最高前面，和后面 CSV 的列序不同，保存时要按列名重新摆放，不能按位置直接当成 open、high、low、close。

```python
rows = []
for item in raw:
    rows.append(
        {
            "date": item[0],
            "open": float(item[1]),
            "high": float(item[3]),
            "low": float(item[4]),
            "close": float(item[2]),
            "volume": float(item[5]),
        }
    )
df = pd.DataFrame(rows)
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date").reset_index(drop=True)
print(df.tail(1))
```

平安银行 `sz000001` 在 2026-10-09 的前复权收盘价是 11.59，成交量约 107.8 万手。完整函数和保存 CSV 的写法在 `examples/fintech/day_k_qq.py`。

## eltdx 日 K

[eltdx](https://pypi.org/project/eltdx/) 走通达信行情协议，不经过上面那个网页接口。先安装：

```
python -m pip install eltdx
```

`TdxClient` 用完要关闭，所以写在 `with` 里。`get_kline` 的第一个参数是周期 `"day"`，`adjust="qfq"` 同样表示前复权。价格在 `bar.open`、`bar.high`、`bar.low`、`bar.close` 上，已经是分开的字段。成交量用 `bar.volume_lots`，单位是手。

```python
from eltdx import TdxClient
import pandas as pd

code = "sz000001"
with TdxClient(timeout=10) as client:
    series = client.get_kline("day", code, count=5, adjust="qfq")

rows = []
for bar in series.bars:
    rows.append(
        {
            "date": bar.time.strftime("%Y-%m-%d"),
            "open": bar.open,
            "high": bar.high,
            "low": bar.low,
            "close": bar.close,
            "volume": bar.volume_lots,
        }
    )
df = pd.DataFrame(rows)
print(df.tail(1))
```

同一次取值里，2026-10-09 的前复权收盘价也是 11.59，成交量约 107.8 万手，和腾讯这一根一致。两条途径可以互相核对；作业里仍然要写明自己用的是哪一条。完整函数在 `examples/fintech/day_k_eltdx.py`。

eltdx 还可以取股票代码和名称。沪深两市在接口里编号是 0 和 1，`category` 为 `a_share` 的才是 A 股：

```python
with TdxClient(timeout=10) as client:
    shown = 0
    for exchange in (0, 1):
        for item in client.get_codes_all(exchange):
            if item.category != "a_share":
                continue
            print(f"{item.exchange}{item.code}", item.name)
            shown += 1
            if shown >= 3:
                break
        if shown >= 3:
            break
```

前三只是：

```
sz000001 平安银行
sz000002 万 科Ａ
sz000006 深振业Ａ
```

知道代码之后，再调用上面的 `get_kline`。quantrader 里对应的文件是 `stock_list_eltdx.py` 和 `day_k_eltdx.py`。

## 保存之后再计算

```python
df.to_csv("sz000001_dayk.csv", index=False)
```

`index=False` 不把行号写进文件。下次打开时用 `read_csv(..., parse_dates=["date"])`，并按日期排序。接口超时或暂时连不上时，用已经保存的 CSV 继续画图和计算。课堂断网时，仍用 `prices.csv`。

下载日期、股票代码和「前复权」写在作业说明里。不要把需要密钥的地址写进公开仓库。

## 课堂练习

1. 用腾讯接口取 `sz000001` 最近 5 根日 K，写出最后一根的日期、收盘价，并说明这一列是前复权。
2. 用 eltdx 取同一只股票的最近 5 根，核对最后一根收盘价是否与腾讯相同。
3. 把不少于 60 根日 K 存成 CSV，列名使用 `date,open,high,low,close,volume`。
