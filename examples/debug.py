# 调试：打印中间结果 / 缩小范围 / pdb
# 对应 docs/debug.md 的几种排查方法

print("--- 打印中间结果 ---")
price = 10
qty = 3
amount = price * qty
print("amount =", amount)

price = 10
qty = 3
tax = 0.1
amount = price * qty
# 金融计算尤其要打印中间量
print("price =", price, "qty =", qty, "tax =", tax)
total = amount * (1 + tax)
print("total =", total)


print("--- 缩小范围：注释一半 ---")
def calc_total(prices):
    # 先把乘法注释掉，只留累加，确认循环本身没错
    total = 0.0
    for p in prices:
        # total = total + p * 1.1
        total = total + p
    return total


print(calc_total([10.0, 20.0, 30.0]))


print("--- 用 assert 检查前提 ---")
def positive(n):
    assert n > 0, "n 必须为正数"
    return n


print(positive(5))
try:
    positive(-1)
except AssertionError as e:
    print("断言失败:", e)

# 想用官方调试器 pdb 时，可这样运行：
#   python -m pdb examples/debug.py
# 命令：n 下一行，p 变量名 查看变量，q 退出
