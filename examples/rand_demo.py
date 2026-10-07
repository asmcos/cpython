# 随机数：randint / random / uniform / choice / sample / shuffle / seed
import random


def show(name):
    print("-" * 12, name, "-" * 12)


show("基础整数和小数")
print(random.randint(1, 10))
print(random.random())
print(random.uniform(0.5, 1.5))

show("从序列里选")
print(random.choice(["a", 1, 43, 544]))
print(random.choices(["a", "b", "c"], k=3))
print(random.sample(range(1, 101), 5))

show("打乱列表")
l = ["432", "hello", 1, "a"]
random.shuffle(l)
print(l)

show("sample 生成新列表，不改原列表")
l = [1, 2, 3, 4]
new = random.sample(l, len(l))
print("原列表:", l)
print("新列表:", new)

show("seed 让结果可复现")
random.seed(7)
print(random.random())
print(random.random())

random.seed(7)
print(random.random())
print(random.random())

show("金融场景：模拟 5 天价格波动")
random.seed(1)
price = 10.0
for day in range(1, 6):
    change = random.uniform(-0.05, 0.05)  # 每天 -5% 到 +5%
    price = price * (1 + change)
    print(f"第{day}天: {price:.2f}")
