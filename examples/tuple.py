t1 = (1, 2, 3, "a")

print(f"t1[0]: {t1[0]}")
print(f"t1[-1]: {t1[-1]}")
print(f"t1[2:4]: {t1[2:4]}")

t2 = (3, 4)
t3 = t1[:2] + t2
print(t3)

l = [1, 2, 3]
print(type(tuple(l)))

t = (1, 2, 3)
print(type(list(t)))
