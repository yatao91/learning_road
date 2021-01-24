#### 1.wait_timeout

> 官方定义:
>
> The number of seconds the server waits for activity on a noninteractive connection before closing it.
>
> On thread startup, the session wait_timeout value is initialized from the global wait_timeout value or from the global interactive_timeout value, depending on the type of client (as defined by the CLIENT_INTERACTIVE connect option to mysql_real_connect())
>
> 即指: 非交互式连接持续时间由wait_timeout进行控制, 即当连接时间超过wait_timeout设置时间后, 此连接断开.

#### 2.interactive_timeout

> 官方定义:
>
> The number of seconds the server waits for activity on an interactive connection before closing it. An interactive client is defined as a client that uses the CLIENT_INTERACTIVE option to mysql_real_connect()
>
> 即指: 交互式连接持续时间由interactive_timeout进行控制, 即当连接时间超过interactive_timeout设置时间后, 此连接端口

#### 3.交互式连接

> 通过MySQL命令行客户端(黑窗口)进行的连接, 称之为交互式连接

#### 4.非交互式连接

> 通常通过jdbc或python的相关的mysql client库进行的连接, 称之为非交互式连接

#### 5.interactive_timeout & wait_timeout继承关系

> 如果是交互式连接, wait_timeout继承全局变量interactive_timeout的值;
>
> 如果是非交互式连接, wait_timeout继承全局变量wait_timeout的值;

#### 6.2013, 'Lost connection to MySQL server during query'

> 此问题的产生原因: 当MySQL wait_timeout设置时间到时, 连接被MySQL 服务器关闭; 但python客户端持有的连接池中的某个连接还没有被回收, 再次使用此连接进行请求MySQL时, 触发此错误.
>
> **解决方案**:
>
> 比如, MySQL server的wait_timtout设置为28800(8小时), 客户端使用sqlalchemy进行连接.
>
> 那么为了避免lost connection问题的出现, 可以设置sqlalchemy的连接配置参数pool_recycle
>
> 设置此值小于wait_timeout即可. 比如可以设置为pool_recycle=3600(一小时)

