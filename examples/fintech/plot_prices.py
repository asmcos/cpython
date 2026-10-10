"""画出收盘价、成交量、均线和收益率直方图。"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import font_manager

for font_path in (
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-SC-Regular.otf",
):
    if Path(font_path).exists():
        font_manager.fontManager.addfont(font_path)
        plt.rcParams["font.family"] = font_manager.FontProperties(fname=font_path).get_name()
        break
plt.rcParams["axes.unicode_minus"] = False

csv_path = Path(__file__).with_name("sz000001_dayk.csv")
out_dir = Path(__file__).resolve().parents[2] / "docs" / "fintech" / "images"
out_dir.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(csv_path, parse_dates=["date"]).sort_values("date")
df["ret"] = df["close"].pct_change()
df["log_ret"] = np.log(df["close"]).diff()
df["ma5"] = df["close"].rolling(5).mean()
df["ma20"] = df["close"].rolling(20).mean()

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(df["date"], df["close"], label="收盘价")
ax.set_title("平安银行前复权收盘价")
ax.set_xlabel("日期")
ax.set_ylabel("价格")
ax.legend()
fig.autofmt_xdate()
fig.tight_layout()
fig.savefig(out_dir / "close.png", dpi=120)
plt.close(fig)

fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(df["date"], df["volume"], width=1.0, label="成交量")
ax.set_title("平安银行成交量（手）")
ax.set_xlabel("日期")
ax.set_ylabel("成交量")
fig.autofmt_xdate()
fig.tight_layout()
fig.savefig(out_dir / "volume.png", dpi=120)
plt.close(fig)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(df["date"], df["close"], label="收盘价")
ax.plot(df["date"], df["ma5"], label="5 日均线")
ax.plot(df["date"], df["ma20"], label="20 日均线")
ax.set_title("收盘价与均线")
ax.set_xlabel("日期")
ax.set_ylabel("价格")
ax.legend()
fig.autofmt_xdate()
fig.tight_layout()
fig.savefig(out_dir / "ma.png", dpi=120)
plt.close(fig)

fig, ax = plt.subplots(figsize=(8, 4))
df["ret"].dropna().hist(bins=15, ax=ax)
ax.set_title("简单收益率分布")
ax.set_xlabel("简单收益率")
ax.set_ylabel("天数")
fig.tight_layout()
fig.savefig(out_dir / "ret_hist.png", dpi=120)
plt.close(fig)

print(df["ret"].describe().to_string())
print("log last", df["log_ret"].iloc[-1])
print("ret last", df["ret"].iloc[-1])
print("ma5 last", df["ma5"].iloc[-1])
print("ma20 last", df["ma20"].iloc[-1])
print("ma5 null", int(df["ma5"].isna().sum()), "ma20 null", int(df["ma20"].isna().sum()))
