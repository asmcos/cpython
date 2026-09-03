# jeapedu · Python 教材

智普教育 [jeapedu.com](https://jeapedu.com) 的大学生 Python 教材。用 MkDocs 生成网站。

教材分两部分：

1. **大学生 Python 入门**：基于 Python 3.12 及以上
2. **金融科技学生学习大纲**：在入门之后学习数据处理、金融计算和量化入门

## 本地预览

请用虚拟环境，避免系统里的 `babel` / `pytz` 混用，以及误装 MkDocs 2.0。

```
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
export NO_MKDOCS_2_WARNING=1
mkdocs serve
```

Windows PowerShell：

```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
$env:NO_MKDOCS_2_WARNING = "1"
mkdocs serve
```

浏览器打开提示的本地地址即可。

`requirements.txt` 把 MkDocs 限制在 1.x。Material 主题目前不能用 MkDocs 2.0。构建时那条 MkDocs 2.0 提示可用 `NO_MKDOCS_2_WARNING=1` 关掉。
