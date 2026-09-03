# 量化分析入门

这一模块只讲「用历史数据验证一个简单规则」。课堂策略不是投资建议，也不能当作实盘系统。

## 要会什么

* 把均线交叉写成持仓信号
* 由持仓得到策略收益
* 计算波动率、最大回撤、夏普比率
* 说清策略的局限：过拟合、交易成本、未来函数

## 均线交叉（教学例子）

短均线上穿长均线视为持有，否则空仓：

```
import pandas as pd

df = pd.read_csv("data/prices.csv", parse_dates=["date"])
df = df.sort_values("date")
df["ret"] = df["close"].pct_change()
df["ma5"] = df["close"].rolling(5).mean()
df["ma20"] = df["close"].rolling(20).mean()
df["position"] = (df["ma5"] > df["ma20"]).astype(int)
df["strategy_ret"] = df["position"].shift(1) * df["ret"]
```

`shift(1)` 很重要：今天的信号，最早明天才能成交。不移位就是在用「当天收盘后才知道的信息」去吃当天的涨跌，这叫未来函数。

## 净值曲线

```
df["equity"] = (1 + df["strategy_ret"].fillna(0)).cumprod()
print(df[["date", "position", "strategy_ret", "equity"]].tail())
```

从 1 开始，看策略资金曲线怎么走。

## 风险指标

```
def max_drawdown(equity):
    peak = equity.cummax()
    dd = equity / peak - 1
    return dd.min()


rets = df["strategy_ret"].dropna()
vol = rets.std(ddof=1)
sharpe = rets.mean() / vol * (252 ** 0.5)
print("vol =", vol)
print("max_drawdown =", max_drawdown(df["equity"]))
print("sharpe =", sharpe)
```

* 波动率：收益波动有多大
* 最大回撤：从高点掉下来最深有多深
* 夏普比率：这里用了年化近似 `sqrt(252)`，作业里必须写明假设

没有无风险利率、没有交易成本时，这些数字只能当练习。

## 必须写进报告的局限

1. 没扣佣金、印花税、滑点
2. 样本外没有验证
3. 只测了一只标的、一段时间
4. 均线参数是事后看到的

老师评分看你是否把这些问题写清楚，不看曲线好不好看。

## 课堂练习

1. 比较「一直持有」和「均线策略」的期末净值。
2. 把 5/20 改成 10/30，观察结果变化。
3. 在报告里用三句话解释最大回撤。
