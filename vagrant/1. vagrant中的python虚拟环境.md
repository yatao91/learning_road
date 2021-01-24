# vagrant + centos中的virtualenv创建虚拟环境问题

### 1. 创建虚拟环境

`virtualenv --no-site-packages environment_name --always-copy`

> 指定python版本
>
> `virtualenv --no-site-packages -p /usr/bin/python2.7 venv2.7 --always-copy`

### 2. 激活虚拟环境

`. environment_name/bin/activate`

### 3. 关闭虚拟环境

`deactivate`

### 4. 官方文档

[virtualenv官方文档](https://link.jianshu.com/?t=http://virtualenv.readthedocs.org/en/latest/virtualenv.html)

### 5. [errno 71] protocol error问题issue

[issue2327](https://github.com/gratipay/gratipay.com/issues/2327)



