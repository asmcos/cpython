# 函数

def display(s):
    print("*" * 5)
    print(s)
    print("-" * 5)


print("--- 定义和调用 ---")
display("hello")
display("jeapedu")

print("--- 返回值 ---")

def add(x, y):
    return x + y


print(add(1, 2))

def label(score):
    if score >= 60:
        return "及格"
    return "不及格"


print(label(75))
print(label(40))

result = display("hello")
print(result)

def divide(a, b):
    return a // b, a % b


print(divide(7, 2))
q, r = divide(7, 2)
print(q, r)

print("--- 默认参数 ---")

def port(p=8080):
    print(f"port = {p}")


port()
port(80)

def host(ip, port=8080):
    print(f"IP is {ip}:{port}")


host("127.0.0.1")
host("127.0.0.1", 80)
host("127.0.0.1", port=80)
host(port=80, ip="127.0.0.1")

print("--- 函数内外的名字 ---")
n = 10

def change(n):
    n = n + 1
    return n


print(change(n))
print(n)

nums = [1, 2]

def append_three(items):
    items.append(3)


append_three(nums)
print(nums)

print("--- 个数不固定 ---")

def total(*nums):
    result = 0
    for n in nums:
        result = result + n
    return result


print(total(10, 20, 30))
print(total())

def show(**info):
    print(info)


show(name="Jike", age=20)

print("--- 默认可变参数会共用 ---")

def add_item(item, bucket=[]):
    bucket.append(item)
    return bucket


print(add_item(1))
print(add_item(2))

def add_item_ok(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


print(add_item_ok(1))
print(add_item_ok(2))
