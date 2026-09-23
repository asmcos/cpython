d = {"a": 1, "b": "hello", "name": "Jike", "age": 21}
print(d)

print(f"d['name']: {d['name']}")

print(d.get("score"))
print(d.get("score", 0))

print("name" in d)
print("score" in d)

for k in d:
    print(k)

for k, v in d.items():
    print(k, v)

print(list(d.keys()))
print(list(d.values()))

b = {"g": [1, 2, 3], "a": 2}
d.update(b)
print(d)

del d["b"]
print(d)

popped = d.pop("age")
print(f"popped: {popped}")
print(d)

print(len(d))

c = d.copy()
c["x"] = 99
print(d)
print(c)

grades = {"Jike": 91, "Anna": 85, "Tom": 91}
scores = {}
for name, score in grades.items():
    scores[score] = name
print(scores)

words = "the cat and the dog and the bird".split()
counter = {}
for w in words:
    counter[w] = counter.get(w, 0) + 1
print(counter)
