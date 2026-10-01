# 错误和异常：try / except / else / finally / raise


def show(name):
    print("-" * 12, name, "-" * 12)


show("try / except")
try:
    print(int("56fdsa7"))
except ValueError:
    print("这不是一个整数")
# 程序不会退出

show("as 拿异常对象")
try:
    print(int("56fdsa7"))
except ValueError as e:
    print(type(e).__name__)
    print(e)

show("多个 except")
def calc(text, divisor):
    try:
        n = int(text)
        return n / divisor
    except ValueError:
        print("不是整数")
    except ZeroDivisionError:
        print("除数是 0")


print(calc("10", 2))
calc("56fdsa7", 2)
calc("10", 0)

show("else 和 finally")
try:
    n = int("567")
except ValueError:
    print("这不是一个整数")
else:
    print("转换成功", n)
finally:
    print("收尾")

show("finally 总是执行")
try:
    n = int("56fdsa7")
except ValueError:
    print("这不是一个整数")
else:
    print("转换成功", n)
finally:
    print("收尾")

show("with 自动关闭")
with open("note.txt", "w", encoding="utf-8") as f:
    f.write("hello")
print("note.txt 已关闭:", f.closed)

show("自己抛出异常")
def check_price(n):
    if n < 0:
        raise ValueError("价格不能是负数")
    return n


print(check_price(10))
try:
    check_price(-1)
except ValueError as e:
    print("接住:", e)
