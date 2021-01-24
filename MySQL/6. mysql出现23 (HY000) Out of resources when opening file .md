mysql 出现 `23 (HY000): Out of resources when opening file `错误的解决办法

+ 运行命令查看linux打开文件限制

  ```
  λ ulimit -n                             
  # 65535
  ```

+ mysql命令行运行`show variables like 'open%';` 命令查看当前打开文件限制数

  ```
  mysql root@127.0.0.1:(none)> show variables like 'open%';
  +------------------+-------+
  | Variable_name    | Value |
  +------------------+-------+
  | open_files_limit | 1024 |
  +------------------+-------+
  1 row in set
  Time: 0.006s
  
  ```


+ /etc/my.conf里面加入open_files_limit = 65535, 重启mysql后无效

+ 在`/etc/systemd/system/mysql.service` 中加入 `LimitNOFILE=65535`

  ```
  [Service]
  User=mysql
  Group=mysql
  
  LimitNOFILE=65535
  # Execute pre and post scripts as root
  PermissionsStartOnly=true
  
  ```

+ 重启mysql, 查看文件限制数,

  ```
  mysql root@127.0.0.1:(none)> show variables like 'open%';
  +------------------+-------+
  | Variable_name    | Value |
  +------------------+-------+
  | open_files_limit | 65535 |
  +------------------+-------+
  1 row in set
  Time: 0.006s
  ```
