# CentOS 7 下安装Redis及持久化配置

安装环境：`CentOS 7.4` 64位，安装 `Redis`。

### 安装

使用`yum`安装

```
yum info redis  // 查看当前源的redis最新版本信息
yum install redis
```

如果不能使用`yum`，可以下载redis的tar.gz文件包，手动编译

```
wget http://download.redis.io/releases/redis-3.2.10.tar.gz

tar -zxvf redis-3.2.10.tar.gz
cd redis-3.2.10
make
make install
```

注意，redis的版本你可以到自己选择，[地址](http://download.redis.io/releases/)

安装成功后，查看`redis-server`的位置。

```
# whereis redis-server
```

### 启动

第一次启动

```
systemctl start redis.service
或者
redis-server
```

启动后，会自动会生成`/etc/redis.conf`文件，如果是自己编译安装的需要拷贝文件到目录`/etc/`, 举例：

```
cd /xxx/redis-3.2.10
cp redis.conf /etc/
```

之后启动可以使用如下命令：

```
redis-server /etc/redis.conf
```

这样你就启动了`redis`了，但是如果你想后台模式启动，需要编辑`vi /etc/redis.conf`文件。

```
daemonize yes
```

### redis的快照和AOF持久化说明

一些简单的配置，比如端口号`port`, 日志位置`logfile`等基本配置可自行配置。

快照RDB持久化配置：

```
# Save the DB on disk:
#  设置sedis进行数据库镜像的频率。
#  900秒（15分钟）内至少1个key值改变（则进行数据库保存--持久化）。
#  300秒（5分钟）内至少10个key值改变（则进行数据库保存--持久化）。
#  60秒（1分钟）内至少10000个key值改变（则进行数据库保存--持久化）。
save 900 1
save 300 10
save 60 10000

stop-writes-on-bgsave-error yes
# 在进行镜像备份时,是否进行压缩。yes：压缩，但是需要一些cpu的消耗。no：不压缩，需要更多的磁盘空间。
rdbcompression yes
# 一个CRC64的校验就被放在了文件末尾，当存储或者加载rbd文件的时候会有一个10%左右的性能下降，为了达到性能的最大化，你可以关掉这个配置项。
rdbchecksum yes
# 快照的文件名
dbfilename dump.rdb
# 存放快照的目录
dir /var/lib/redis
```

AOF持久化配置：

```
# 是否开启AOF，默认关闭（no）
appendonly yes
# 指定 AOF 文件名
appendfilename appendonly.aof
# Redis支持三种不同的刷写模式：
# appendfsync always #每次收到写命令就立即强制写入磁盘，是最有保证的完全的持久化，但速度也是最慢的，一般不推荐使用。
appendfsync everysec #每秒钟强制写入磁盘一次，在性能和持久化方面做了很好的折中，是受推荐的方式。
# appendfsync no     #完全依赖OS的写入，一般为30秒左右一次，性能最好但是持久化最没有保证，不被推荐。

#在日志重写时，不进行命令追加操作，而只是将其放在缓冲区里，避免与命令的追加造成DISK IO上的冲突。
#设置为yes表示rewrite期间对新写操作不fsync,暂时存在内存中,等rewrite完成后再写入，默认为no，建议yes
no-appendfsync-on-rewrite yes 
#当前AOF文件大小是上次日志重写得到AOF文件大小的二倍时，自动启动新的日志重写过程。
auto-aof-rewrite-percentage 100
#当前AOF文件启动新的日志重写过程的最小值，避免刚刚启动Reids时由于文件尺寸较小导致频繁的重写。
auto-aof-rewrite-min-size 64mb
```

**快照RDB和AOF持久化如何选择呢：**

1）如果能接受几分钟的数据丢失的话，建议选择快照RDB 2）要是不允许数据丢失，则需要用AOF来持久化

**关于数据恢复：** RDB的启动时间会更短，原因有两个： 一是RDB文件中每一条数据只有一条记录，不会像AOF日志那样可能有一条数据的多次操作记录。所以每条数据只需要写一次就行了。 另一个原因是RDB文件的存储格式和Redis数据在内存中的编码格式是一致的，不需要再进行数据编码工作，所以在CPU消耗上要远小于AOF日志的加载。

**注意：** AOF(Append Only File)<二进制文件>比RDB方式有更好的持久化性。由于在使用AOF持久化方式时，Redis会将每一个收到的写命令都通过Write函数追加到文件最后，类似于MySQL的binlog。 AOF的完全持久化方式同时也带来了另一个问题，持久化文件会变得越来越大。(比如我们调用INCR test命令100次，文件中就必须保存全部的100条命令，但其实99条都是多余的。因为要恢复数据库的状态其实文件中保存一条SET test 100就够了)。为了合并重写AOF的持久化文件，Redis提供了bgrewriteaof命令。

**Redis重启如何载入数据的：**

通过日志可以很清楚的知道redis通过那个文件来取数据的：

```
RDB: * DB loaded from disk: 0.000 seconds
AOF: * DB loaded from append only file: 0.000 seconds
```

保存数据则是：

```
RDB: * DB saved on disk
AOF: * Calling fsync() on the AOF file.
```

重启时将按照以下优先级恢复数据到内存：

```
•如果只配置AOF,重启时加载AOF文件恢复数据。
•如果同时 配置了RBD和AOF,启动是只加载AOF文件恢复数据。
•如果只配置RBD,启动是讲加载dump文件恢复数据。
```

如果你先开启了RDB模式，想再开启AOF模式，先执行`bgrewriteaof`命令，不然会因为恢复数据的优先级问题，数据都没有了。

为了防止悲剧发生，注意**多备份**，AOF模式，记得使用脚本定期执行`bgrewriteaof`命令。

脚本如下，可以结合`Linux Crontab`来使用，定期执行。

```
echo 'bgrewriteaof redis 6379'
redis-cli -p 6379 bgrewriteaof
```