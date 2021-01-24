##### 问题描述

> 使用命令`python -m unittest`执行单元测试时, 出现下述问题
>
> ```
> /lib/python3.6/importlib/_bootstrap.py:219: ImportWarning: can't resolve package from __spec__ or __package__, falling back on __name__ and __path__
>   return f(*args, **kwds)
> ```

##### 解决方式一

> 可以使用以下命令来忽略此种类型错误
>
> `python -W ignore:ImportWarning -m unittest`
>
> 但无法解决根本问题

##### 解决方式二

> 在`setUp`方法中增加如下代码来忽略此种警告信息
>
> ```
>     def setUp(self):
>         """测试初始化"""
> 
>         # 忽略ImportWarning
>         warnings.simplefilter('ignore', category=ImportWarning)
> ```
>
> 也无法解决根本问题

##### 相关问题

> [astropy-issue6025](https://github.com/astropy/astropy/issues/6025)
>
> [so](https://stackoverflow.com/questions/51045319/how-to-suppress-importwarning-in-a-python-unittest-script)

