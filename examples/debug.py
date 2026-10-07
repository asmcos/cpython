# 调试：打印中间结果 / 缩小范围 / assert / pdb / logging
# 对应 docs/debug.md

print("--- 打印中间结果 ---")
price = 10
qty = 3
amount = price * qty
print("amount =", amount)

price = 10
qty = 3
tax = 0.1
amount = price * qty
print("price =", price, "qty =", qty, "tax =", tax)
total = amount * (1 + tax)
print("total =", total)


print("--- 缩小范围：注释一半 ---")
def calc_total(prices):
    total = 0.0
    for p in prices:
        total = total + p  # 先把乘以税率的步骤注释掉
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


print("--- 用 logging（进阶） ---")
import logging

logging.basicConfig(level=logging.INFO)
logging.debug("只在 debug 级别显示")
logging.info("正常信息")
logging.warning("警告")


print("--- 金融场景：核对每一步计算 ---")
def future_value(pv, r, n):
    print("pv =", pv, "r =", r, "n =", n)
    step = 1 + r
    print("step =", step)
    result = pv * step ** n
    print("result =", result)
    return result


print(future_value(10000, 0.05, 3))

# 想用官方调试器 pdb 时，可这样运行：
#   python -m pdb examples/debug.py
# 命令：n 下一行，p 变量名 查看变量，q 退出
