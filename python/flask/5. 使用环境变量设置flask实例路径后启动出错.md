# 当使用环境变量设置flask的APP后,flask run出错

### 1. 出错过程

设置flask环境变量: `export FLASK_APP=flask_app`

使用`flask run`启动报错

`Error: The file/path provided (flaskr) does not appear to exist.`

### 2. 解决办法

flask版本过低, 卸载并升级到最新版本1.0.2版本后问题得到解决

`pip uninstall flask`

`pip install flask`

### 3. 参考网上问题

[参考](https://stackoverflow.com/questions/41913345/flask-error-the-file-path-provided-does-not-appear-to-exist-although-the-file)

