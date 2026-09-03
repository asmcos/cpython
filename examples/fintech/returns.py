import numpy as np

prices = np.array([10.0, 10.5, 10.2, 11.0])
returns = prices[1:] / prices[:-1] - 1

print(returns)
print(returns.mean(), returns.std(ddof=1))
