+ 安装和设置mysql
    + 安装Mysql Yum Repository
    ```
    wget https://repo.mysql.com/mysql57-community-release-el7-11.noarch.rpm
    sudo rpm -Uvh mysql57-community-release-el7-11.noarch.rpm
    ```
    + 安装Mysql
    ```
    sudo yum install mysql-community-server -y
    ```
    + 设置mysql
    ```
    sudo service mysqld start 
    # 通过如下命令找到mysql root 初始密码
    sudo grep 'temporary password' /var/log/mysqld.log
    mysql -uroot -p
    # 卸载复杂密码插件
    ALTER USER 'root'@'localhost' IDENTIFIED BY 'Root1234@';
    UNINSTALL PLUGIN validate_password; 
    # 设置新密码
    ALTER USER 'root'@'localhost' IDENTIFIED BY '123456';
    ```
    + 设置远程登录
    ```
    use mysql;
    GRANT ALL ON *.* to root@'%' IDENTIFIED BY '123456';
    FLUSH PRIVILEGES;
    ```
    + 修改防火墙, 参考[CentOS 7 下开启Mysql-5.7.19远程访问](https://blog.csdn.net/u010758410/article/details/76381632)
    ```
    sudo firewall-cmd --zone=public --add-port=3306/tcp --permanent
    sudo firewall-cmd --reload
    ```
    + 开机启动
    ```
    sudo chkconfig mysqld on
    ```
    + 数据库目录备份拷贝或者更改位置后, 需要用`*chown* -R *mysql*:*mysql*` 更改权限

        ```
        chown -R mysql:mysql /var/lib/mysql
        ```

    + 参考

        + [CentOS 安装Mysql 5.7](https://www.jianshu.com/p/b913dbb16e57)
        + [CentOS 7.0下使用yum安装MySQL](https://segmentfault.com/a/1190000015216149)
        + [MySQL 5.7 初始密码和密码复杂度问题](http://blog.itpub.net/29773961/viewspace-2077579/)
        + [Index of Yum](https://repo.mysql.com/)


+ 安装和设置redis
    + 安装
    ```
    sudo yum update
    sudo yum install epel-release
    sudo yum install redis
    ```
    + 开启远程登录
        + 修改配置文件, /etc/redis.conf,
        找到`bind 127.0.0.1`, 改成`bind 0.0.0.0`,
        找到`protected-mode yes`, 改成`protected-mode no`
        + 防火墙开放端口
        ```
        sudo firewall-cmd --zone=public --add-port=6379/tcp --permanent
        sudo firewall-cmd --reload
        ```
    + 启动redis
    ```
    sudo service redis start
    ```
    + 设置开机启动
    ```
    sudo chkconfig redis on
    ```
    + 参考
        + [centos7 安装redis服务器](https://blog.csdn.net/jjlovefj/article/details/77802376)
        + [centos 7 redis远程连接](https://blog.csdn.net/u011482763/article/details/77991516)
    
  + 开启x11
    + 修改sshd_config配置文件
    ```
    X11Forwarding yes
    ```
    + 安装相关包
    ```
    sudo yum -y install xorg-x11-xauth xorg-x11-utils
    sudo yum groupinstall fonts
    ```
    + wsl 通过ssh -X链接到centos
    ```
    ssh -X xin@centos_ip
    ```
    + 参考
        + [RHEL CENTOS ORACLE LINUX 7.x设置X11转发到XManager](https://blog.csdn.net/gzliudan/article/details/50564881)
        + [Creating a minimally viable Centos instance for SSH X11 Forwarding](https://justaprogrammer.net/2013/05/19/creating-a-minimally-viable-centos-instance-for-ssh-x11-forwarding/)
  
  + 安装virtualbox 增强
    + 依赖包
    ```
    sudo yum install -y kernel-devel gcc bzip2 tar 
    ```
    + 挂载光驱
    ```
    sudo mount /dev/cdrom /media
    ```
    + 安装
    ```
    sudo ./VBoxLinuxAdditions.run
    ```
    + 参考
        + [centos7.3安装增强工具](http://blog.51cto.com/laoyinga/1887947) 
  
  + virtualbox 设置共享
    +  添加用户到vboxsf中
    ```
    sudo usermod -aG vboxsf $(whoami)
    ```
    + 重启centos, virtualbox设置要共享的文件夹
    + 将共享的文件夹软连接到home用户目录下
    ```
    sudo ln -s /media/sf_data /home/xin/d
    ```