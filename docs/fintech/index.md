# 第二部分：金融科技

本章面向金融科技专业的读者。后续无论分析行情，还是计算现金流，都需要你亲手完成；因此，先掌握一门能够把它们写下来、算出来的语言，会很重要。如果你还没有 Python 基础，建议先阅读 [《Python 入门》](../part1/index.md)，再回到本章。讲义收录于 [jeapedu.com](https://jeapedu.com)。

本章学习内容包括：用 Pandas 读写行情表，整理自己的日行情，画价格和均线，计算收益、现值、投资组合和 β，再用二叉树、Black-Scholes 和蒙特卡洛给看涨期权定价。学期末交一份可以按说明重新跑出来的小项目。

学完后应达到：

1. 能读写 CSV / Excel，完成清洗和分组
2. 能整理一份日行情，并写清来源、频率和复权口径
3. 能计算简单收益、对数收益、复利、现值和 NPV
4. 能按目标收益配置两种资产，估计 β，并在证券市场线上读出期望收益
5. 能用一步二叉树、Black-Scholes 和蒙特卡洛给看涨期权定价，并写明各自的假设
6. 能画出价格和均线，估计波动率和 95% 历史模拟风险价值
7. 能独立完成一个小项目，说明数据从哪来、怎么算、结果是什么

平时作业里的买卖信号用来核对计算。成绩看数据能否按说明重跑、数字是否正确、结论是否和结果一致。

## 参考课程

下面是几门可以对照着看的公开课纲：

* 香港大学 [FINA2390 Financial Programming and Databases](https://ug.hkubs.hku.hk/f/course/255404/25_26-FINA2390.pdf)
* 香港中文大学金融硕士 [Python in Finance](https://masters.bschool.cuhk.edu.hk/programmes/mscfin/)
* 香港科技大学 [FINA5240 FinTech Analytics](https://mfin.hkust.edu.hk/the-program/curriculum)
* 香港科技大学公开课 [Python and Statistics for Financial Analysis](https://www.coursera.org/learn/python-statistics-financial-analysis)
* 香港城市大学 [FB6710 Practical FinTech Applications](https://www.cityu.edu.hk/catalogue/pg/202425/course/FB6710B.htm)
* 香港理工大学 [AF3214 Python Programming for Accounting and Finance](https://www.polyu.edu.hk/af/-/media/department/af/content/study/subject-syllabi/ug/2024/af3214_20241.pdf)
* 哥伦比亚大学 [MATH GR5260 Programming for Quantitative and Computational Finance](https://www.math.columbia.edu/~kyn/GR5260%20syllabus%20spring%202026.pdf)
* 纽约大学 [FRE-GY 6811 Financial Software Laboratory（Python）](https://engineering.nyu.edu/sites/default/files/2024-11/fre-6811_kamdem_fall_2024_syllabus.pdf)
* 伦敦政治经济学院 [FM442 Quantitative Methods for Finance and Risk Analysis](https://www.lse.ac.uk/resources/calendar2026-2027/courseGuides/FM/2026_FM442.htm)

## 先修与工具

* Python 3.12 及以上
* 第一部分里的函数、文件、异常、pip / venv
* 微积分、概率统计、公司金融可以边学边补

```
python -m venv .venv
python -m pip install pandas numpy matplotlib openpyxl requests
```

| 库 | 用途 |
| --- | --- |
| `numpy` | 数组和向量计算 |
| `pandas` | 表格、时间序列 |
| `matplotlib` | 画图 |
| `openpyxl` | 读写 Excel |
| `requests` | 需要更新行情时再发请求 |

## 十六周进度

每周按 4 课时加课外上机。学校课表不同，可以按模块压缩，不要打乱顺序：先算得动一张表，再去取数。

### 第 1 周：方向和工具

* 金融科技里 Python 常见用途：对账、研报数据、风控指标、量化研究、内部报表
* 复习第一部分：函数、文件、异常、venv
* 建课程目录 `fintech-lab/`
* 作业：写出本学期想解决的一个具体问题，不超过 200 字

### 第 2–4 周：把表算对

这三周用教材自带的 `examples/fintech/prices.csv`，先不要依赖网络。

* 第 2 周：[NumPy 数组](numpy.md)、[用数组算收益率](numpy_returns.md)。作业：用数组算一组价格的简单收益率，并写出 `std(ddof=1)`。
* 第 3 周：[Series 与 DataFrame](pandas_frame.md)、[读表、筛选和清洗](pandas_io.md) 的前半。作业：读入 CSV，打印前 5 行、列名和收盘价最高的日期。
* 第 4 周：清洗空值、重复行，以及 [分组汇总](pandas_group.md)。作业：按月份汇总成交量，写出交易日天数。

### 第 5–6 周：取得自己的行情

说明见 [金融数据获取](data.md)。先认清日期、开高低收和成交量，用本地文件把读取跑通，再把下载结果存成 CSV。后面的计算读这份文件。

* 第 5 周：日期、开高低收、成交量；解析日期、排序。作业：整理至少 60 个交易日，写明复权口径。
* 第 6 周：把下载结果收成 CSV。接口失败时，用已经保存的文件继续后面的课。

### 第 7–8 周：画图和时间序列

说明见 [可视化与时间序列](viz.md)。

* 第 7 周：收盘价曲线、成交量。作业：一张价格图、一张成交量图，横轴是日期。
* 第 8 周：简单收益、对数收益、5 日和 20 日均线。作业：同一张图上画出收盘价和两条均线。

### 第 9–10 周：投资组合

说明见 [投资组合与证券市场线](portfolio.md)。[金融计算](calc.md) 里的复利和 NPV 留一道手算题，本周作业以组合为主。

* 第 9 周：两种资产、目标收益、组合标准差。作业：给定收益和相关系数，算出权重和风险。
* 第 10 周：用股票和指数的收益估计 β，画出证券市场线。本周选定期末题目，见 [学期项目](project.md)。

### 第 11–12 周：收益风险，以及一条对照用的均线

说明见 [收益分布与风险价值](risk.md) 和 [量化分析入门](quant.md)。

* 第 11 周：波动率、95% 历史模拟风险价值、最大回撤。
* 第 12 周：均线信号和 `shift(1)`。作业比较「一直持有」和这条规则的净值，并写明没扣费用。

### 第 13–14 周：期权

说明见 [期权定价](options.md)。取数函数见 [网络接口](api.md)，本周把下载结果存成文件即可。

* 第 13 周：一步二叉树。作业：改涨跌幅度，重算风险中性概率和价格。
* 第 14 周：Black-Scholes 公式，以及同一组参数下的蒙特卡洛价格。两份结果放在一起，写明路径条数和随机种子。

### 第 15–16 周：项目答辩

* 演示 8–10 分钟：问题、数据、方法、结果、局限
* 提交代码、数据说明、不超过 6 页的报告

## 考核

| 项目 | 比例 | 说明 |
| --- | --- | --- |
| 平时作业 | 40% | 每周一小练，交代码和结果 |
| 阶段测验 | 20% | Pandas + 一题金融计算 |
| 期末项目 | 40% | 能复现、有数据说明、结论和数字一致 |

## 学习方法

1. 第 2–4 周只动本地 CSV，把筛选、汇总、收益率算对。
2. 第 5 周起再取自己的行情，取到就存盘。
3. 金融数字用 Excel 或计算器对一次。
4. 第 10 周前选定题目，不要留到最后两周。

下一节从 [NumPy 数组](numpy.md) 开始处理表格。
