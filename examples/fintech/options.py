import math

import numpy as np


def norm_cdf(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def binomial_call(s, k, u, d, r):
    su = s * u
    sd = s * d
    cu = max(su - k, 0.0)
    cd = max(sd - k, 0.0)
    q = ((1 + r) - d) / (u - d)
    return (q * cu + (1 - q) * cd) / (1 + r)


def black_scholes_call(s, k, t, r, sigma):
    d1 = (math.log(s / k) + (r + 0.5 * sigma**2) * t) / (sigma * math.sqrt(t))
    d2 = d1 - sigma * math.sqrt(t)
    return s * norm_cdf(d1) - k * math.exp(-r * t) * norm_cdf(d2)


def mc_call(s, k, t, r, sigma, n, seed):
    rng = np.random.default_rng(seed)
    z = rng.standard_normal(n)
    st = s * np.exp((r - 0.5 * sigma**2) * t + sigma * math.sqrt(t) * z)
    payoff = np.maximum(st - k, 0.0)
    return math.exp(-r * t) * payoff.mean()


print("binomial =", round(binomial_call(100, 100, 1.1, 0.9, 0.02), 4))
print("bs =", round(black_scholes_call(100, 100, 1.0, 0.02, 0.20), 4))
print("mc =", round(mc_call(100, 100, 1.0, 0.02, 0.20, 20000, 7), 4))
