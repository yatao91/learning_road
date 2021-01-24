#### 一. 关于utf-8

> `utf-8`Unicode Transformation Format-8bit。是用以解决国际上字符的一种多字节编码。
>
> > 它对英文使用8位（即一个字节) ，中文使用24位（三个字节）来编码。
>
> `UTF-8`包含全世界所有国家需要用到的字符，是国际编码，通用性强。
>
> `UTF-8`编码的文字可以在各国支持UTF8字符集额的浏览器上显示。 如果是`UTF8`编码，则在外国人的英文IE也能显示中文，他们无需下载IE的中文语言支持包。

#### 二. 关于GBK

>`GBK` 是国家标准GB2312基础上扩容后兼容GB2312的标准。
>`GBK`的文字编码是用双字节来表示的，即不论中、英文字符均使用双字节来表示，为了区分中文，将其最高位都设定成1。
>`GBK`包含全部中文字符，是国家编码，通用性比UTF8差，不过UTF8占用的数据库比`GBK`大。

#### 三. 关于utf8mb4

>MySql 5.5 之前，UTF8 编码只支持1-3个字节，只支持BMP这部分的unicode编码区，BMP是从哪到哪？ [戳这里](http://en.wikipedia.org/wiki/Mapping_of_Unicode_characters) 基本就是 0000 ~ FFFF 这一区。
>
>从MySQL 5.5 开始，可支持4个字节UTF编码utf8mb4，一个字符最多能有4字节，所以能支持更多的字符集。
>
>```
>utf8mb4 is a superset of utf8
>```
>
>tf8mb4兼容utf8，且比utf8能表示更多的字符。
>至于什么时候用，看你做的什么项目了。。。 在做移动应用时，会遇到`IOS`用户在文本的区域输入`emoji`表情，如果不做一定处理，就会导致插入数据库异常。

#### 四. 汉字长度与编码有关

> MySql 5.0 以上的版本：
>
> 1、一个汉字占多少长度与编码有关：
>
> - UTF-8：一个汉字 = 3个字节，英文是一个字节
> - GBK： 一个汉字 = 2个字节，英文是一个字节
>
> 2、varchar(n) 表示n个字符，无论汉字和英文，`MySql`都能存入 `n` 个字符，仅实际字节长度有所区别。
>
> 3、MySQL检查长度，可用SQL语言
>
> ```mysql
> SELECT LENGTH(fieldname) FROM tablename
> ```

#### 五. 实际测试

>1、首先使用`utf8` 创建 `str_test` 表。
>
>```
>CREATE TABLE `str_test` (
>    `name_chn` varchar(20) NOT NULL,
>    `name_en`  varchar(20) NOT NULL
>) ENGINE=InnoDB AUTO_INCREMENT=62974 DEFAULT CHARSET=utf8
>```
>
>然后插入值
>
>```
>mysql> insert into  str_test values ('我爱Ruby', 'I Love Ruby!');
>Query OK, 1 row affected (0.02 sec)
>```
>
>打开irb
>
>```
>>> "我爱Ruby".size
>=> 6
>>> "I Love Ruby!".size
>=> 12
>>>
>```
>
>从MySQL中查询出来的结果，对比
>
>```
>mysql> select * from str_test;
>+------------+--------------+
>| name_chn   | name_en      |
>+------------+--------------+
>| 我爱Ruby   | I Love Ruby! |
>+------------+--------------+
>1 row in set (0.02 sec)
>
>
>mysql> select length(name_chn) from str_test;
>+------------------+
>| length(name_chn) |
>+------------------+
>|               10 |
>+------------------+
>1 row in set (0.01 sec)
>```
>
>3[一个汉字三字节] * 2 + 1[一个英文一字节] * 4 = 10
>
>```
>mysql> select length(name_en) from str_test;
>+-----------------+
>| length(name_en) |
>+-----------------+
>|              12 |
>+-----------------+
>1 row in set (0.00 sec)
>```
>
>10[一个英文一字节] * 1 + 2[空格一字节] * whitespace = 12
>
>2、使用 `GBK` 做测试
>
>创建表
>
>```
>    CREATE TABLE `str_test` (
>    `name_chn` varchar(20) NOT NULL,
>    `name_en`  varchar(20) NOT NULL
>) ENGINE=InnoDB AUTO_INCREMENT=62974 DEFAULT CHARSET=gbk
>```
>
>插入数据，并且测试
>
>```
>mysql> insert into  str_test values ('我爱Ruby', 'I Love Ruby!');
>Query OK, 1 row affected (0.00 sec)
>
>mysql> select * from str_test;
>+------------+--------------+
>| name_chn   | name_en      |
>+------------+--------------+
>| 我爱Ruby   | I Love Ruby! |
>+------------+--------------+
>1 row in set (0.01 sec)
>```
>
>`GBK` 中文是两个字节，英文是一个字节。
>
>```
>mysql> select length(name_chn) from str_test;
>+------------------+
>| length(name_chn) |
>+------------------+
>|                8 |
>+------------------+
>1 row in set (0.00 sec)
>```
>
>2[中文两个字节] * 2 + 4[英文一个字节] * 1 = 8
>
>```
>mysql> select length(name_en) from str_test;
>+-----------------+
>| length(name_en) |
>+-----------------+
>|              12 |
>+-----------------+
>1 row in set (0.00 sec)
>```
>
>10[英文一个字节] * 1 + 2[空格一个字节] * whitespace = 12

#### 六. 关于varchar最多能存多少值

> - mysql的记录行长度是有限制的，不是无限长的，这个长度是`64K`，即`65535`个字节，对所有的表都是一样的。
> - MySQL对于变长类型的字段会有1-2个字节来保存字符长度。
> - 当字符数小于等于255时，MySQL只用1个字节来记录，因为2的8次方减1只能存到255。
> - 当字符数多余255时，就得用2个字节来存长度了。
> - 在`utf-8`状态下的varchar，最大只能到 (65535 - 2) / 3 = 21844 余 1。
> - 在`gbk`状态下的varchar, 最大只能到 (65535 - 2) / 2 = 32766 余 1
>
> 使用 `utf-8` 创建
>
> ```
> mysql>     CREATE TABLE `str_test` (
> ->         `id`  tinyint(1)  NOT NULL,
> ->         `name_chn` varchar(21845) NOT NULL
> ->     ) ENGINE=InnoDB AUTO_INCREMENT=62974 DEFAULT CHARSET=utf8
> -> ;
> ERROR 1118 (42000): Row size too large. The maximum row size for the used table type, not counting BLOBs, is 65535. This includes storage overhead, check the manual. You have to change some columns to TEXT or BLOBs
> mysql>     CREATE TABLE `str_test` (
> ->         `id`  tinyint(1)  NOT NULL,
> ->         `name_chn` varchar(21844) NOT NULL
> ->     ) ENGINE=InnoDB AUTO_INCREMENT=62974 DEFAULT CHARSET=utf8
> ->
> ->
> -> ;
> Query OK, 0 rows affected (0.06 sec)
> ```
>
> 使用`gbk`创建
>
> 当存储长度为 32768 失败~
>
> ```
>     mysql>     CREATE TABLE `str_test` (
>     ->         `id`  tinyint(1)  NOT NULL,
>     ->         `name_chn` varchar(32768) NOT NULL
>     ->     ) ENGINE=InnoDB AUTO_INCREMENT=62974 DEFAULT CHARSET=gbk
>     -> ;
> ERROR 1074 (42000): Column length too big for column 'name_chn' (max = 32767); use BLOB or TEXT instead
> ```
>
> 当存储长度为 32767 失败~
>
> ```
> mysql>     CREATE TABLE `str_test` (                                                                                                 ->         `id`  tinyint(1)  NOT NULL,
>     ->         `name_chn` varchar(32767) NOT NULL
>     ->     ) ENGINE=InnoDB AUTO_INCREMENT=62974 DEFAULT CHARSET=gbk
>     -> ;
> ERROR 1118 (42000): Row size too large. The maximum row size for the used table type, not counting BLOBs, is 65535. This includes storage overhead, check the manual. You have to change some columns to TEXT or BLOBs
> ```
>
> 当存储长度为 32766 成功~
>
> ```
> mysql>     CREATE TABLE `str_test` (
>     ->         `id`  tinyint(1)  NOT NULL,
>     ->         `name_chn` varchar(32766) NOT NULL
>     ->     ) ENGINE=InnoDB AUTO_INCREMENT=62974 DEFAULT CHARSET=gbk
>     -> ;
> Query OK, 0 rows affected (0.03 sec)
> ```
>
> smallint 用两个字节存储，所以
>
> 2[smallint] + 32766 * 2[varchar存储长度] + 2[2个字节来存长度] > 65535
>
> 所以失败~
>
> ```mysql
> mysql>     CREATE TABLE `str_test` (
>     ->         `id`  smallint(1)  NOT NULL,
>     ->         `name_chn` varchar(32766) NOT NULL
>     ->     ) ENGINE=InnoDB AUTO_INCREMENT=62974 DEFAULT CHARSET=gbk
>     -> ;
> ERROR 1118 (42000): Row size too large. The maximum row size for the used table type, not counting BLOBs, is 65535. 
> ```

#### 七. 数值类型所占的字节

> | 类型     | 所占字节 |
> | -------- | -------- |
> | int      | 4 字节   |
> | smallint | 2 字节   |
> | tinyint  | 1 字节   |
> | decimal  | 变长     |
>
> 官方关于`decimal` 的描述如下
>
> > Values for DECIMAL (and NUMERIC) columns are represented using a binary format that packs nine decimal (base 10) digits into four bytes.
> > Storage for the integer and fractional parts of each value are determined separately.
> > Each multiple of nine digits requires four bytes, and the “leftover” digits require some fraction of four bytes.
> > The storage required for excess digits is given by the following table.
>
> 翻译为中文
>
> > 使用二进制格式将9个十进制(基于10)数压缩为4个字节来表示DECIMAL列值。
> > 每个值的整数和分数部分的存储分别确定。
> > 每个9位数的倍数需要4个字节，并且“剩余的”位需要4个字节的一部分。
> > 下表给出了超出位数的存储需求：
>
> | Leftover Digits | Number Of Bytes |
> | --------------- | --------------- |
> | 0               | 0               |
> | 1               | 1               |
> | 2               | 1               |
> | 3               | 2               |
> | 4               | 2               |
> | 5               | 3               |
> | 6               | 3               |
> | 7               | 4               |
> | 8               | 4               |
>
> **那：decimal(10,2)占几个字节？**
>
> 1、首先 10 指的是整数与小数部分的总长度， 2指的是小数部分的长度。那么整数部分就只有 10 - 2 = 8 位
>
> 2、因为整数与小数的存储市各自独立确定的，所以他们各自所占用空间的综合就是所占的总空间了。
>
> 3、对表可知，整数部分8位占了4个字节，小数部分2位占了1个字节，所以decimal(10,2)总共占了 4 + 1 = 5 个字节。
>
> 4、decimal(6,2) 整数部分(6 - 2 = 4) 位占2字节，小数部分2位占1字节，总共占3字节。

#### 八. 总结

> varchar 字段是将实际内容单独存储在聚簇索引之外，内容开头用1到2个字节表示实际长度（长度超过255时需要2个字节），因此最大长度不能超过65535。
>
> - UTF-8：一个汉字 = 3个字节，英文是一个字节
> - GBK： 一个汉字 = 2个字节，英文是一个字节
>
> 在`utf-8`状态下，汉字最多可以存 **21844**个字符串, 英文也为 **21844**个字符串。
>
> 在`gbk`状态下，汉字最多可以存 **32766**个字符串，英文也为 **32766**个字符串。

#### 参考

---

[MySQL 数据库 varchar 到底可以存多少个汉字，多少个英文呢?我们来搞搞清楚](https://ruby-china.org/topics/24920)