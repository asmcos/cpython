"""腾讯前复权日 K。代码形如 sz000001、sh600000。"""

import json
import re
from pathlib import Path

import pandas as pd
import requests


def fetch_qq_dayk(code, count=320):
    code = code.replace(".", "").lower()
    url = "https://proxy.finance.qq.com/ifzqgtimg/appstock/app/newfqkline/get"
    resp = requests.get(
        url,
        params={"_var": "kline_dayqfq", "param": f"{code},day,,,{count},qfq"},
        timeout=15,
    )
    resp.raise_for_status()
    resp.encoding = "utf-8"
    # \s 空白，* 零次或多次，$ 到结尾；DOTALL 让 . 也能匹配换行。
    # 圆括号里是要交给 json.loads 的那一段。
    match = re.search(r"kline_dayqfq\s*=\s*({.*})\s*$", resp.text, re.DOTALL)
    if not match:
        raise ValueError("腾讯返回里没有 kline_dayqfq")
    payload = json.loads(match.group(1))
    raw = payload["data"][code].get("qfqday") or payload["data"][code].get("day") or []
    rows = []
    for item in raw:
        if len(item) < 6:
            continue
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
    return df.sort_values("date").reset_index(drop=True)


if __name__ == "__main__":
    code = "sz000001"
    df = fetch_qq_dayk(code, count=5)
    print(df)
    out = Path(__file__).with_name(f"{code}_qq.csv")
    df.to_csv(out, index=False)
    print(out.name)
