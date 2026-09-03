# 安装其他模块

第三方模块发布在 https://pypi.org/ ，用 pip 安装。

Python 3.12 请用下面的方式，不要用 `sudo pip install`。那样容易把系统环境弄乱。

## 先建虚拟环境

在项目目录里：

```
python -m venv .venv
```

激活环境：

* Windows：`.venv\Scripts\activate`
* macOS / Linux：`source .venv/bin/activate`

激活后，命令行前面通常会出现 `(.venv)`。

## 安装

```
python -m pip install requests
```

这会安装网络请求库 `requests`。第二部分金融科技课会用到它。

升级 pip 本身：

```
python -m pip install -U pip
```

## 在代码里引用

```
import requests
```

这是 Python 代码，不是命令行。

## 查看已安装的包

```
python -m pip list
```

后面做金融科技练习时，还会安装 `pandas`、`matplotlib` 等库。仍然在虚拟环境里用 `python -m pip install` 安装。
