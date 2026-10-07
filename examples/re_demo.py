# 正则：findall / search / sub / split / 分组
import re


def show(name):
    print("-" * 12, name, "-" * 12)


show("findall 找全部")
print(re.findall("cat", "The cat and the dog sat on the mat"))
print(re.findall("ca.", "cat and car"))
print(re.findall("o.", "good morning"))
print(re.findall(r"\d\d", "qq:12345,phone:323"))
print(re.findall(r"\w\w", "qq:12345,phone:323"))

show("个数：* + ?")
print(re.findall(r":\d*", "qq:12345"))
print(re.findall(r":\d*", "qq:"))
print(re.findall(r":\d+", "qq:12345"))
print(re.findall(r":\d+", "qq:"))
print(re.findall(r":\d?", "qq:12345"))
print(re.findall(r":\d?", "qq:"))

show("search 找第一个")
m = re.search(r"\d+", "价格是 58 元")
print(m.group())

m = re.search(r"\d+", "没有数字")
print(m)

show("sub 替换")
print(re.sub(r"\d+", "XX", "订单 123 价格 45"))
print(re.sub(r"\s", "", "SH 600600"))

show("split 切分")
print(re.split(r"[,;]", "10,20;30,40"))

show("分组：括号")
print(re.findall(r"(\d+)元", "苹果5元，梨3元"))

m = re.search(r"(\d+)年(\d+)月", "成立于2020年6月")
print(m.group(1))
print(m.group(2))

show("金融场景：从交易流水提取信息")
line = "买入 600600 数量2000 价格39.95"
m = re.search(r"数量(\d+)\s+价格([\d.]+)", line)
if m:
    qty = int(m.group(1))
    price = float(m.group(2))
    print(f"数量 {qty}，价格 {price}，金额 {qty * price:.2f}")
