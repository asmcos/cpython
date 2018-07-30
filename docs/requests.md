# requests

>requests 是我使用的python库里面最棒的http client库。

安装
---

```
$ pipenv install requests
```

源代码
-----

```
https://github.com/requests/requests
```

文档
----

>  http://docs.python-requests.org/


本文档选择写requests主要是 ，requests太好用了。我要整理出来，如果能用golang实现一个类似的，那就实现了我的梦想。

开始使用
-------

`` get ``

```
import requests
resp = requests.get("http://cpython.org")
print(resp.content)
```

这里``resp`` 是从 http 网络的返回 的response ， content就是网页内容。


``post``

你可以可以发送一个post请求，一般post请求都要上传一些参数（数据），例子如下。来自官网文档。
因为我也没有合适的例子。


```
 resp = requests.post('http://httpbin.org/post', data = {'key':'value'})
```


`` 其他请求``

HTTP 请求类型：PUT，DELETE，HEAD 以及 OPTIONS,例子来自官方文档。

```
>>> r = requests.put('http://httpbin.org/put', data = {'key':'value'})
>>> r = requests.delete('http://httpbin.org/delete')
>>> r = requests.head('http://httpbin.org/get')
>>> r = requests.options('http://httpbin.org/get')

```

URL 参数
--------

通常情况，你看到的网址 http://httpbin.org/get?key2=value2&key1=value1

get请求带参数的 ``URL`` 例子：

```
>>> payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

>>> r = requests.get('http://httpbin.org/get', params=payload)
>>> print(r.url)
http://httpbin.org/get?key1=value1&key2=value2&key2=value3
```

查看返回结果
==========

```
In [5]: import requests

In [6]: r = requests.get('http://cpython.org')

In [7]: r.text
Out[7]: u'<!DOCTYPE html>\n<!--[if IE 8]><html c................
```

r.status_code 表示返回状态，例如：200, 404,500 等


JSON 数据格式
=============

```
>>> import requests

>>> r = requests.get('https://api.github.com/events')
>>> r.json()
[{u'repository': {u'open_issues': 0, u'url': 'https://github.com/...
```

自定义请求头
-----------

```
>>> url = 'http://www.jeapedu.com'
>>> headers = {'user-agent': 'my-app/0.0.1'}

>>> r = requests.get(url, headers=headers)
```

POST Multipart-Encoded 文件
----------------------------

```
>>> url = 'http://httpbin.org/post'
>>> files = {'file': open('report.xls', 'rb')}

>>> r = requests.post(url, files=files)
>>> r.text
{
  ...
  "files": {
    "file": "<censored...binary...data>"
  },
  ...
}
```

Cookies
---------

``获取返回的cookies``

```
>>> url = 'http://example.com/some/cookie/setting/url'
>>> r = requests.get(url)

>>> r.cookies['example_cookie_name']
'example_cookie_value'
```

``设置一个cookies 项``

```
>>> url = 'http://httpbin.org/cookies'
>>> cookies = dict(cookies_are='working')

>>> r = requests.get(url, cookies=cookies)
>>> r.text
'{"cookies": {"cookies_are": "working"}}'
```


``CookieJar``

```
>>> jar = requests.cookies.RequestsCookieJar()
>>> jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
>>> jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
>>> url = 'http://httpbin.org/cookies'
>>> r = requests.get(url, cookies=jar)
>>> r.text
'{"cookies": {"tasty_cookie": "yum"}}'
```

我还写了requests[源代码注释](http://www.cpython.org/requests_notes/index.html)
