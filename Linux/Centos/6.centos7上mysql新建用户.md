# centos7上mysql新建用户
+ 1: 关闭防火墙

```
systemctl stop firewalld.service #停止firewall
systemctl disable firewalld.service #禁止firewall开机启动

```

+ 2: 设置mysql开机启动

```
chkconfig mysqld on
```

参考[link](http://blog.phpha.com/backup/archives/1458.html)

+ 3: 用设置的root密码登录后 增加新的user和密码

```
CREATE USER 'pig'@'%' IDENTIFIED BY '123456';

```

其中'pig'是新的user名, '@'是任何ip都可以登录, '123456'是密码


+ 4: 开启远程登录,

```
Grant all privileges on *.* to 'pig'@'%' identified by '123456' with grant option;
flush privileges; #刷新生效
```

+ 5: 验证是否创建成功

```
use mysql;
select host,user from user;
```

