# 配置好nginx后浏览器请求接口出现502错误

#### 问题描述

公司目前新开了一台微软的服务器, 然后按照前期在阿里云服务器上部署的方式, 将项目进行了部署. 在配置完nginx后, 发现通过公网域名及对应项目端口无法访问, 报502错误.

#### 解决步骤

> 1. 因为本身对nginx不熟悉, 当时认为是nginx配置出现了问题, 但对比阿里云机器上的配置, 并没有什么不同, 且监听的8080端口是正常开放的. 并无其他问题.
> 2. 开始向日志求助, 发现日志记录了`13: Permission denied`错误信息. 前期未遇到过此类问题.
>
> ![1548662524970](C:\Users\46081\AppData\Roaming\Typora\typora-user-images\1548662524970.png)
>
> 3. 带着日志中的错误信息, 去Google上进行了搜索, 在StackOverflow上找个一个同样的问题.[参考](https://stackoverflow.com/questions/23948527/13-permission-denied-while-connecting-to-upstreamnginx), 按照帖子上的命令执行之后, 解决了问题.

#### 具体原因查找

> 微软服务器上默认开启了SELinux, 并且`httpd_can_network_connect: off`是关闭状态. 
>
> 阿里云服务器上默认关闭了SELinux. 所以不受SELinux安全策略的影响.

#### SELinux

> 安全增强式Linux（SELinux，Security-Enhanced Linux）是一个Linux内核的安全模组，其提供了访问控制安全策略机制，包括了美国国防部风格的强制访问控制（Mandatory Access Control，MAC）。
>
> SELinux是一系列添加到多个Linux发行版的内核修改与用户空间工具。其软件架构力图从安全策略中分离出执行安全决策并优化涉及执行安全策略的软件。奠基SELinux的核心概念可以追溯回美国国家安全局（NSA）的一些早期项目。

#### 解决办法

> 开启http network connect
>
> `setsebool httpd_can_network_connect on`
>
> 永久开启
>
> `setsebool httpd_can_network_connect on -P`
>
> 查看httpd相关的SELinux选项
>
> `getsebool -a | grep httpd`

[参考](https://stackoverflow.com/questions/23948527/13-permission-denied-while-connecting-to-upstreamnginx)

