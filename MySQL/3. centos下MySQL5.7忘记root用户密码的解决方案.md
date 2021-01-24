#### 1. 修改MySQL登录设置

> `vim /etc/my.cnf`
>
> 在`[mysqld]`的段中加上一句: `skip-grant-tables`
>
> 保存并退出.

#### 2. 重新启动mysql

> `service mysqld restart`

#### 3. 登录并修改MySQL的root账户密码

> `mysql`
>
> `use mysql`
>
> `UPDATE user SET authentication_string = password("123456") WHERE user = "root"`

#### 4. 删掉`skip-grant-tables`, 然后重启mysql

#### 5. 然后使用更改后的密码进行登录即可.