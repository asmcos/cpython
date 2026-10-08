import numpy as np

prices = np.array([10.0, 10.5, 10.2, 11.0])
returns = prices[1:] / prices[:-1] - 1

print(prices[1:])
print(prices[:-1])
print(returns)
print(returns.mean())
print(returns.std(ddof=1))
print(returns.std(ddof=0))
