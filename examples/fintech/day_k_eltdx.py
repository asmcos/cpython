"""通达信 eltdx 前复权日 K。需要 pip install eltdx。"""

import sys
from pathlib import Path

import pandas as pd

try:
    from eltdx import TdxClient
except ImportError:
    print("请先安装: python -m pip install eltdx")
    sys.exit(1)


def fetch_eltdx_dayk(code, count=320, adjust="qfq"):
    code = code.replace(".", "").lower()
    with TdxClient(timeout=10) as client:
        series = client.get_kline("day", code, count=count, adjust=adjust)
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
    df["date"] = pd.to_datetime(df["date"])
    return df.sort_values("date").reset_index(drop=True)


if __name__ == "__main__":
    code = "sz000001"
    df = fetch_eltdx_dayk(code, count=5)
    print(df)
    out = Path(__file__).with_name(f"{code}_eltdx.csv")
    df.to_csv(out, index=False)
    print(out.name)
