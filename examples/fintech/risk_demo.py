from pathlib import Path

import numpy as np
import pandas as pd

csv_path = Path(__file__).with_name("prices.csv")
df = pd.read_csv(csv_path, parse_dates=["date"]).sort_values("date")
df["ret"] = df["close"].pct_change()
df["log_ret"] = np.log(df["close"]).diff()
log_ret = df["log_ret"].dropna()

print(log_ret.describe())
print("mean =", float(log_ret.mean()))
print("std =", float(log_ret.std(ddof=1)))
print("ann_vol =", float(log_ret.std(ddof=1) * np.sqrt(252)))

q = float(log_ret.quantile(0.05))
print("5% quantile =", q)
print("95% historical VaR =", -q)

rng = np.random.default_rng(7)
mu = float(log_ret.mean())
sigma = float(log_ret.std(ddof=1))
price0 = float(df["close"].iloc[-1])
drawn = rng.normal(mu, sigma, size=252)
path = price0 * np.exp(np.cumsum(drawn))
print("start =", price0)
print("end =", float(path[-1]))

ends = []
for _ in range(500):
    drawn = rng.normal(mu, sigma, size=252)
    ends.append(price0 * np.exp(np.cumsum(drawn)[-1]))
ends = np.array(ends)
print("median end =", float(np.median(ends)))
print("5% end =", float(np.quantile(ends, 0.05)))
