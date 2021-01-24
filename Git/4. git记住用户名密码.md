# Git记住用户名密码

HTTPS方式每次都需要输入用户名密码.可以使用如下设置来记住密码

1. 首先执行下面的命令(如果不执行可能设置无效)

   ```
   git config --global user.email "你的邮箱"
   git config --global user.name "你的名字"
   ```

2. 执行如下命令可以在输入密码后记住用户名密码

   ```
   1. 设置记住密码(默认15分钟)
   git config --global credential.helper cache
   
   2. 可以自己设置过期时间
   git config credential.helper 'cache --timeout=3600'
   
   3. 长期存储密码(一般自己的机器用这个比较方便)
   git config --global credential.helper store
   
   4. 增加远程地址的时候带上密码也可以
   http://yourname:password@git.oschina.net/name/project.git
   ```


