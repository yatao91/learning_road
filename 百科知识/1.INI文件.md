#### 简介

> **`INI`文件**是一个无固定格式的配置文件. 它以简单的文字与简单的结构组成, 常常使用在Windows操作系统, 或者其他系统上. 许多程序也会采用`INI`文件作为配置文件使用. 
>
> `INI`文件的命名来源: 是取自英文"初始(`Initial`)"的首字母缩写-----初始化程序的意思. 
>
> `INI`文件也会以不同的扩展名代替, 比如: `.CFG`/`.CONF`/`.TXT`.

#### 格式

###### 节

> `[section]`

###### 参数

> `name=value`

###### 注解

> 注解使用分好表示(;). 在分号后面的文字, 直到该行结尾都全部为注解. 
>
> `; comment text`

#### 示例

> 下面示例: 有两个小节
>
> 前面的小节用来设置拥有者的信息
>
> 后面的小节用来设置数据库的位置
>
> 前面的注释记录谁最后编辑此文件
>
> 而后面的注释记录为何不使用域名而是使用IP地址
>
> ```
> ; last modified 1 April 2001 by John Doe
> [owner]
> name=John Doe
> organization=Acme Products
> 
> [database]
> server=192.0.2.42 ; use IP address in case network name resolution is not working
> port=143
> file="acme payroll.dat"
> ```

#### 参考

> [INI文件]([https://zh.wikipedia.org/wiki/INI文件](https://zh.wikipedia.org/wiki/INI%E6%96%87%E4%BB%B6))