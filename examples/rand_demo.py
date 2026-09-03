import random

print(random.randint(1, 10))
print(random.random())
print(random.choice(["a", 1, 43, 544]))

l = ["432", "hello", 1, "a"]
random.shuffle(l)
print(l)
