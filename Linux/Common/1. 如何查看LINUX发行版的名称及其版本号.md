### 一. 查看Linux内核版本命令

> 1. `cat /proc/version`
>
>    ```
>    ~# cat /proc/version
>    Linux version 3.10.0-862.11.6.el7.x86_64 (builder@kbuilder.dev.centos.org) (gcc version 4.8.5 20150623 (Red Hat 4.8.5-28) (GCC) ) #1 SMP Tue Aug 14 21:49:04 UTC 2018
>    ```
>
> 2.  `uname -a`
>
>    ```
>    ~# uname -a
>    Linux  3.10.0-862.11.6.el7.x86_64 #1 SMP Tue Aug 14 21:49:04 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
>    ```

#### 二. 查看Linux系统版本的命令

> 1. `lsb_release -a`, 即可列出所有版本信息:
>
>    ```
>    ~# lsb_release -a
>    LSB Version:	:core-4.1-amd64:core-4.1-noarch
>    Distributor ID:	CentOS
>    Description:	CentOS Linux release 7.5.1804 (Core) 
>    Release:	7.5.1804
>    Codename:	Core
>    ```
>
>    这个命令适用于所有的Linux发行版, 包括Redhat/SUSE/Debian等
>
> 2. `cat /etc/redhat-release`, 这种方法只适合Redhat系列的Linux.
>
>    ```
>    ~# cat /etc/redhat-release 
>    CentOS Linux release 7.5.1804 (Core)
>    ```
>
> 3. `cat /etc/issue`, 此命令也适用于所有的Linux发行版.
>
>    ```
>    /usr/sbin# cat /etc/issue
>    Ubuntu 18.04.2 LTS \n \l
>    ```

#### 三. 引用

> [如何查看LINUX发行版的名称及其版本号](https://www.qiancheng.me/post/coding/show-linux-issue-version)

