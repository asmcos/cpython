d = {}
d["a"] = 1
d["b"] = "hello"
d["name"] = "Jike"
d["age"] = 21

print(d)

for k in d.keys():
    print(k, d[k])

b = {"g": [1, 2, 3], "a": 2}
d.update(b)
print(d)

del d["b"]
print(d)

for k, v in d.items():
    print(k, v)
