#### 1.简介

> binlog是MySQLserver层维护的一种二进制日志.
>
> 主要用来记录对MySQL数据更新或潜在发生更新的SQL语句, 并以'事务'的形式保存在磁盘中.
>
> **作用**:
>
> - 复制: MySQL replication在master端开启binlog, master把它的二进制日志传递给slaves并回放以达到主从一致的目的.
> - 数据恢复: 通过mysqlbinlog工具恢复数据
> - 增量备份

#### 2.binlog配置及使用

> - **开启binlog**
>
>   ```
>   # 配置MySQL配置文件:my.cnf
>   vim my.cnf
>   
>   datadir=/var/lib/mysql  # MySQL数据目录
>   log-bin=suyatao-bin  # binlog日志名前缀,若没有给出,则使用mysql-bin来命名
>   max_binlog_size=200M  # binlog日志文件最大限制, 默认1G
>   binlog_format=mixed  # 配置binlog日志格式,默认为mixed.总共有row/statement/mixed
>   
>   # 重启MySQL服务
>   service mysqld restart
>   
>   # 查看binlog配置信息
>   mysql> show global variables like '%log_bin%';
>   +---------------------------------+----------------------------------+
>   | Variable_name                   | Value                            |
>   +---------------------------------+----------------------------------+
>   | log_bin                         | ON                               |
>   | log_bin_basename                | /var/lib/mysql/mysql-bin       |
>   | log_bin_index                   | /var/lib/mysql/mysql-bin.index |
>   | log_bin_trust_function_creators | OFF                              |
>   | log_bin_use_v1_row_events       | OFF                              |
>   +---------------------------------+----------------------------------+
>   5 rows in set (0.01 sec)
>   ```
>
> - **查看binlog状态**
>
>   ```
>   # 查看binlog文件列表
>   mysql> show binary logs;
>   +--------------------+-----------+-----------+
>   | Log_name           | File_size | Encrypted |
>   +--------------------+-----------+-----------+
>   | mysql-bin.000001 |       155 | No        |
>   +--------------------+-----------+-----------+
>   1 row in set (0.00 sec)
>   
>   # 查看当前binlog日志信息:文件名 当前位置等
>   mysql> show master status;
>   +------------------+----------+--------------+------------------+-------------------+
>   | File             | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
>   +------------------+----------+--------------+------------------+-------------------+
>   | mysql-bin.000001 |      155 |              |                  |                   |
>   +------------------+----------+--------------+------------------+-------------------+
>   1 row in set (0.00 sec)
>   
>   # 清空binlog日志文件
>   mysql> reset master;
>   Query OK, 0 rows affected (0.01 sec)
>   
>   # 查看binlog日志记录
>   mysql> show binlog events;
>   
>   | Log_name         | Pos | Event_type     | Server_id | End_log_pos | Info     
>   | mysql-bin.000001 |   4 | Format_desc    |         1 |         124 | Server ver: 8.0.17, Binlog ver: 4 |
>   | mysql-bin.000001 | 124 | Previous_gtids |         1 |         155 |         
>   2 rows in set (0.01 sec)
>   ```
>
> - **binlog内容的查看**
>
>   ```
>   # 1.使用MySQL官方提供的mysqlbinlog工具进行查看
>   [root@worker001 mysql]# mysqlbinlog /var/lib/mysql/mysql-bin.000001 
>   /*!50530 SET @@SESSION.PSEUDO_SLAVE_MODE=1*/;
>   /*!50003 SET @OLD_COMPLETION_TYPE=@@COMPLETION_TYPE,COMPLETION_TYPE=0*/;
>   DELIMITER /*!*/;
>   # at 4  # position位置. 事件起点
>   #190808  5:44:18 server id 1  end_log_pos 124 CRC32 0x9497bcfb 	Start: binlog v 4, server v 8.0.17 created 190808  5:44:18 at startup
>   # Warning: this binlog is either in use or was not closed properly.
>   ROLLBACK/*!*/;
>   BINLOG '
>   srZLXQ8BAAAAeAAAAHwAAAABAAQAOC4wLjE3AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
>   AAAAAAAAAAAAAAAAAACytktdEwANAAgAAAAABAAEAAAAYAAEGggAAAAICAgCAAAACgoKKioAEjQA
>   CgH7vJeU
>   '/*!*/;
>   # at 124
>   #190808  5:44:18 server id 1  end_log_pos 155 CRC32 0xc50f83fe 	Previous-GTIDs
>   # [empty]
>   SET @@SESSION.GTID_NEXT= 'AUTOMATIC' /* added by mysqlbinlog */ /*!*/;
>   DELIMITER ;
>   # End of log file
>   /*!50003 SET COMPLETION_TYPE=@OLD_COMPLETION_TYPE*/;
>   /*!50530 SET @@SESSION.PSEUDO_SLAVE_MODE=0*/;
>   
>   # 2.直接mysql-client命令行查看
>   # 格式: SHOW BINLOG EVENTS [IN 'log_name'] [FROM pos] [LIMIT [offset,], row_count]
>   mysql> show binlog events in 'mysql-bin.000001';
>   +------------------+-----+----------------+-----------+-------------+-----------------------------------+
>   | Log_name         | Pos | Event_type     | Server_id | End_log_pos | Info                              |
>   +------------------+-----+----------------+-----------+-------------+-----------------------------------+
>   | mysql-bin.000001 |   4 | Format_desc    |         1 |         124 | Server ver: 8.0.17, Binlog ver: 4 |
>   | mysql-bin.000001 | 124 | Previous_gtids |         1 |         155 |                                   |
>   +------------------+-----+----------------+-----------+-------------+-----------------------------------+
>   2 rows in set (0.05 sec)
>   ```
>
> - **导出binlog日志文件内容**
>
>   ```
>   # 使用mysqlbinlog导出binlog日志文件
>   [root@worker001 mysql]# mysqlbinlog mysql-bin.000001 > /root/out.txt
>   
>   格式如下:
>   mysqlbinlog --start-position=4 --stop-position=585 mysql-bin.000001 > /root/out
>   ```

#### 3.binlog日志模式

> - **STATEMENT**:记录每一条修改数据的SQL语句(批量修改时,记录的不是单条SQL语句, 而是批量修改的SQL语句事件)
>
>   ```
>   优点:statement模式记录的是更改的SQL语句事件, 并非每条更改记录. 所以大大减少了binlog日志量, 节约磁盘IO, 提高性能.
>   缺点:statement模式下对一些特殊功能的复制效果不是很好, 比如:函数/存储过程的复制. 由于row模式是基于每一行的变化来记录的, 所以不会出现类似问题.
>   ```
>
>   
>
> - **ROW**:记录的方式是行, 即如果批量修改数据, 记录的不是批量修改的SQL语句事件, 而是每条记录被修改的SQL语句.ROW模式的binlog日志文件会变得很重.
>
>   ```
>   优点: row level的binlog日志内容非常清楚的记录下每一行数据被修改的细节. 而且不会出现某些特定情况下存储过程或function以及trigger的调用和触发器无法被正确复制的问题.
>   缺点:row level下, 所有执行的语句当记录到日志的时候, 都以每行记录的修改来记录. 这样可能产生大量的日志内容.产生的binlog日志量是惊人的. 
>   ```
>
>   
>
> - **MIXED**
>
>   ```
>   实际上是前两种的结合. 在MIXED模式下, MySQL会根据执行的每一条具体的SQL语句来区分对待记录的日志形式, 也就是在STATEMENT和ROW之间选择一种
>   ```
>
> - **如何选择binlog模式**
>
>   - 如果生产中使用MySQL特殊功能相对较少(存储过程/触发器/函数). 选择默认模式:STATEMENT LEVEL
>   - 如果生产中使用MySQL特殊功能较多的, 可以选择MIXED模式
>   - 如果生产中使用MySQL特殊功能较多, 又希望数据最大化一致, 最好选择ROW模式. 但是需要注意, 该模式的binlog会非常重.
>
>   