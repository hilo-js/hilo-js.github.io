hilojs.com
==========

Site of Hilojs

## 编写教程

* 编写教程
    * 所有教程源文件都必须在 `tutorail_src` 目录下。
    * 教程格式为`Markdown`。
* 编译教程
    * 参照 `mkdocs/requirements.txt` 安装所有依赖，比如：`easy_install install Jinja2` 或 `pip install Jinja2`。
    * 运行 `mkdocs/mkdocs build --config=tutorial.yml`。
    * 若编译正确，编译后的教程文档可在 `tutorial` 里找到。