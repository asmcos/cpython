# 网络接口（requests）

`requests` 是常用的 HTTP 客户端。金融科技里用它拉公开数据、调内部服务、提交表单。

先安装：

```
python -m pip install requests
```

官方文档：https://requests.readthedocs.io/

## GET

```
import requests

resp = requests.get("https://httpbin.org/get", timeout=10)
print(resp.status_code)
print(resp.text[:200])
```

`resp.status_code` 是状态码，例如 200、404、500。`resp.text` 是文本，`resp.content` 是字节。

课堂示例用 `httpbin.org` 或学校指定的接口。不要把密钥写进教材仓库。

## 带查询参数

```
payload = {"key1": "value1", "key2": ["value2", "value3"]}
r = requests.get("https://httpbin.org/get", params=payload, timeout=10)
print(r.url)
```

这和你在浏览器里看到的 `?key1=value1&key2=value2` 是一回事。

## JSON

很多金融接口返回 JSON：

```
r = requests.get("https://httpbin.org/json", timeout=10)
data = r.json()
print(type(data))
```

`r.json()` 通常得到字典或列表，再交给 `pandas.DataFrame`。

## POST 和请求头

```
r = requests.post(
    "https://httpbin.org/post",
    json={"symbol": "DEMO", "days": 30},
    headers={"User-Agent": "jeapedu-class/0.1"},
    timeout=10,
)
print(r.status_code)
```

访问 [jeapedu.com](https://jeapedu.com) 时也可以自定义请求头：

```
r = requests.get(
    "https://jeapedu.com",
    headers={"User-Agent": "jeapedu-class/0.1"},
    timeout=10,
)
print(r.status_code)
```

## 超时和异常

网络会断。请求必须写 `timeout`，并且接住异常：

```
try:
    r = requests.get("https://httpbin.org/delay/1", timeout=3)
    r.raise_for_status()
except requests.RequestException as e:
    print("请求失败", e)
```

`raise_for_status()` 会在 4xx、5xx 时抛错。

## 收成函数

```
def fetch_json(url, params=None):
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    return r.json()
```

作业要求：下载一次、存成 CSV、之后的计算全部读本地文件。

## Cookies（了解即可）

```
r = requests.get("https://httpbin.org/cookies/set/session/demo", timeout=10)
print(r.cookies.get("session"))
```

登录态、会话这些到具体项目再展开。入门先把 GET、JSON、超时写对。
