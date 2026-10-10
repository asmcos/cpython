from pathlib import Path

import pandas as pd

csv_path = Path(__file__).with_name("prices.csv")
df = pd.read_csv(csv_path, parse_dates=["date"])
print(df.head(3))
print(df.dtypes)
print(len(df))

df = df.sort_values("date")
high = df[df["close"] >= 10.8]
print(high[["date", "close"]])

best = df.loc[df["close"].idxmax()]
print(best["date"].date(), best["close"])

raw = pd.DataFrame(
    {
        "date": ["2024-01-02", "2024-01-02", "2024-01-03"],
        "close": ["10.10", "10.10", None],
        "volume": ["100", None, "80"],
    }
)
print(raw["close"].dtype)
raw["close"] = pd.to_numeric(raw["close"])
raw["volume"] = pd.to_numeric(raw["volume"]).fillna(0)
raw = raw.dropna(subset=["close"])
raw = raw.drop_duplicates(subset=["date"])
print(raw)
