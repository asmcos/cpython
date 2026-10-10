import numpy as np

prices = np.array([10.0, 10.5, 10.2, 11.0])
print(prices)
print(type(prices))
print(prices.dtype)
print(prices.shape)
print(prices.ndim)
print(len(prices))

print(prices[0])
print(prices[-1])
print(prices[1:3])

print(prices + 1)
print(prices * 2)

a = [1, 2, 3]
b = [10, 20, 30]
print(a + b)
print(np.array(a) + np.array(b))
