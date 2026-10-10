import numpy as np
import pandas as pd

close = pd.Series([10.0, 10.5, 10.2], name="close")
print(close)
print(close.mean())

date = pd.Series(["2024-01-02", "2024-01-03", "2024-01-04"], name="date")
volume = pd.Series([1000, 1200, 800], name="volume")
df = pd.DataFrame({"date": date, "close": close, "volume": volume})
print(df)
print(type(df["close"]).__name__)

by_col = pd.DataFrame(
    {
        "date": ["2024-01-02", "2024-01-03", "2024-01-04"],
        "close": [10.0, 10.5, 10.2],
        "volume": [1000, 1200, 800],
    }
)
print(by_col)

by_row = pd.DataFrame(
    [
        {"date": "2024-01-02", "close": 10.0, "volume": 1000},
        {"date": "2024-01-03", "close": 10.5, "volume": 1200},
        {"date": "2024-01-04", "close": 10.2, "volume": 800},
    ]
)
print(by_row)

rows = [
    ["2024-01-02", 10.0, 1000],
    ["2024-01-03", 10.5, 1200],
    ["2024-01-04", 10.2, 800],
]
print(pd.DataFrame(rows, columns=["date", "close", "volume"]))

arr = np.array([[10.0, 1000], [10.5, 1200], [10.2, 800]])
print(pd.DataFrame(arr, columns=["close", "volume"]))

close_col = df["close"]
print(type(close_col).__name__)
print(close_col)

part = df[["date", "close"]]
print(type(part).__name__)
print(part.shape)

only = df[["close"]]
print(type(only).__name__)
print(only.shape)

print(close_col.mean())
print(df[["close", "volume"]].mean())

df["ret"] = df["close"].pct_change()
print(df)

print(df.iloc[0])
print(df.loc[1, "close"])

df["date"] = pd.to_datetime(df["date"])
print(df.dtypes)
