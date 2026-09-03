def future_value(pv, r, n):
    return pv * (1 + r) ** n


def present_value(fv, r, n):
    return fv / (1 + r) ** n


def annuity_fv(pmt, r, n):
    return pmt * ((1 + r) ** n - 1) / r


def npv(rate, cashflows):
    total = 0.0
    for t, cf in enumerate(cashflows):
        total += cf / (1 + rate) ** t
    return total


if __name__ == "__main__":
    print(future_value(10000, 0.05, 3))
    print(present_value(11576.25, 0.05, 3))
    print(annuity_fv(1000, 0.05, 3))
    print(npv(0.1, [-1000, 400, 400, 400]))
