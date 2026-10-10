import math


def weight_for_target(mu1, mu2, target):
    return (target - mu2) / (mu1 - mu2)


def portfolio_sigma(w, s1, s2, rho):
    var = w**2 * s1**2 + (1 - w) ** 2 * s2**2 + 2 * w * (1 - w) * rho * s1 * s2
    return math.sqrt(var)


w = weight_for_target(0.10, 0.04, 0.07)
sigma = portfolio_sigma(w, 0.20, 0.10, 0.20)
print("w =", w)
print("sigma =", round(sigma, 4))

r = [0.02, -0.01, 0.03, 0.01]
m = [0.01, -0.02, 0.04, 0.02]
n = len(r)
mean_r = sum(r) / n
mean_m = sum(m) / n
cov = sum((r[i] - mean_r) * (m[i] - mean_m) for i in range(n)) / (n - 1)
var_m = sum((m[i] - mean_m) ** 2 for i in range(n)) / (n - 1)
beta = cov / var_m
rf = 0.02
premium = 0.06
expected = rf + beta * premium
print("beta =", round(beta, 4))
print("sml =", round(expected, 4))
