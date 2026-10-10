from pathlib import Path

import pandas as pd

csv_path = Path(__file__).with_name("prices.csv")
df = pd.read_csv(csv_path, parse_dates=["date"]).sort_values("date")
df["ret"] = df["close"].pct_change()
df["month"] = df["date"].dt.to_period("M")

monthly = df.groupby("month", as_index=False).agg(
    volume=("volume", "sum"),
    close_last=("close", "last"),
    days=("close", "size"),
)
print(monthly)

out = Path(__file__).with_name("monthly_volume.csv")
monthly.to_csv(out, index=False)
print(out.name)
