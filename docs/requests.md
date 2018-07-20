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

```
import requests
resp = requests.get("http://cpython.org")
print(resp.content)
```
