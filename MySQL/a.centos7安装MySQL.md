## 通过YUM仓库安装MySQL

#### 1.添加MySQL YUM仓库

> a.下载MySQL yum repo[https://dev.mysql.com/downloads/repo/yum/](https://dev.mysql.com/downloads/repo/yum/)
>
> b. 选择适合你系统的版本包, 此处下载`mysql80-community-release-el7-3.noarch.rpm`
>
> c. 安装下载下来的版本包, 将添加MySQL yum repo到系统的repo list中.
>
> > `sudo yum localinstall mysql80-community-release-el7-3.noarch.rpm`
>
> d. 检查MySQL yum repo是否成功添加
>
> > ```
> > [root@worker001 ~]# yum repolist enabled | grep "mysql.*-community.*"
> > mysql-connectors-community/x86_64 MySQL Connectors Community                 118
> > mysql-tools-community/x86_64      MySQL Tools Community                       95
> > mysql80-community/x86_64          MySQL 8.0 Community Server                 129
> > ```
>
> e. `yum update`

#### 2.选择要安装的MySQL版本

> a.列出所有可用的MySQL子repo
>
> > ```
> > [root@worker001 yum.repos.d]# yum repolist all | grep mysql
> > mysql-cluster-7.5-community/x86_64 MySQL Cluster 7.5 Community   disabled
> > mysql-cluster-7.5-community-source MySQL Cluster 7.5 Community - disabled
> > mysql-cluster-7.6-community/x86_64 MySQL Cluster 7.6 Community   disabled
> > mysql-cluster-7.6-community-source MySQL Cluster 7.6 Community - disabled
> > mysql-cluster-8.0-community/x86_64 MySQL Cluster 8.0 Community   disabled
> > mysql-cluster-8.0-community-source MySQL Cluster 8.0 Community - disabled
> > mysql-connectors-community/x86_64  MySQL Connectors Community    enabled:    118
> > mysql-connectors-community-source  MySQL Connectors Community -  disabled
> > mysql-tools-community/x86_64       MySQL Tools Community         enabled:     95
> > mysql-tools-community-source       MySQL Tools Community - Sourc disabled
> > mysql-tools-preview/x86_64         MySQL Tools Preview           disabled
> > mysql-tools-preview-source         MySQL Tools Preview - Source  disabled
> > mysql55-community/x86_64           MySQL 5.5 Community Server    disabled
> > mysql55-community-source           MySQL 5.5 Community Server -  disabled
> > mysql56-community/x86_64           MySQL 5.6 Community Server    disabled
> > mysql56-community-source           MySQL 5.6 Community Server -  disabled
> > mysql57-community/x86_64           MySQL 5.7 Community Server    disabled
> > mysql57-community-source           MySQL 5.7 Community Server -  disabled
> > mysql80-community/x86_64           MySQL 8.0 Community Server    enabled:    129
> > mysql80-community-source           MySQL 8.0 Community Server -  disabled
> > ```
>
> b.配置需要安装的版本
>
> > ```
> > # 不安装MySQL80
> > [root@worker001 yum.repos.d]# sudo yum-config-manager --disable mysql80-community
> > # 安装MySQL57
> > [root@worker001 yum.repos.d]# sudo yum-config-manager --enable mysql57-community
> > ```
>
> c.除了上述这种通过`yum-config-manager`来选择安装版本repo外, 还可以通过如下方式:
>
> > ```
> > vim /etc/yum.repo.d/mysql-community.repo
> > [mysql57-community]
> > name=MySQL 5.7 Community Server
> > baseurl=http://repo.mysql.com/yum/mysql-5.7-community/el/7/$basearch/
> > enabled=1  # 0-代表不使用此repo 1-代表使用此repo
> > gpgcheck=1
> > gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-mysql
> > ```
>
> d.确认选择的repo是否是正确的
>
> > ```
> > [root@worker001 yum.repos.d]# yum repolist enabled | grep mysql
> > mysql-connectors-community/x86_64 MySQL Connectors Community                 118
> > mysql-tools-community/x86_64      MySQL Tools Community                       95
> > mysql57-community/x86_64          MySQL 5.7 Community Server                 364
> > ```

#### 3.安装MySQL

> `sudo yum install mysql-community-server`

#### 4.MySQLserver的控制

> ```
> # 启动mysql服务
> sudo service mysqld start
> 
> # 查看mysql服务状态
> sudo service mysqld status
> 
> # 停止mysql服务
> sudo service mysqld stop
> 
> # 重启mysql服务
> sudo service mysqld restart
> ```

#### 5.获取root用户临时密码

> ```#
> # 获取MySQL root用户临时密码
> sudo grep 'temporary password' /var/log/mysqld.log
> 
> # 登录mysql
> mysql -uroot -p
> 
> # 修改root用户密码
> ALTER USER 'root'@'localhost' IDENTIFIED BY 'your password';
> ```

#### 6.卸载密码验证器

> 注意: 如果没有修改root临时密码, 则无法卸载密码验证器
>
> ```
> UNINSTALL COMPONENT 'file://component_validate_password';
> ```

