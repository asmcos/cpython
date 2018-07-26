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
