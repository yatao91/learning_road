+ centos 单机安装kafka教程,  参考 [Setup a single Apache Kafka node on CentOS 7](https://progressive-code.com/post/19/Setup-a-single-Apache-Kafka-node-on-CentOS-7)

+ 配置参数

  ```
  # 自动生成topic, 默认是true, 生产环境需要改成false
  auto.create.topics.enable=false
  # 自动删除topic, 默认是true
  delete.topic.enable=true
  ```

+ 注意:
  + 配置项前后不能有空格
  + topic name 最好不要使用_ 和. 用- 

+ 查看所有的topic
  ```shell
  bin/kafka-topics.sh --zookeeper 127.0.0.1:2181 --list
  ```

+ 创建topic
  ```shell
  bin/kafka-topics.sh --zookeeper 127.0.0.1:2181 --create --topic ggzy --partitions 8  --replication-factor 1 --config max.message.bytes=10485760
  bin/kafka-topics.sh --zookeeper 127.0.0.1:2181 --create --topic ccgp --partitions 8  --replication-factor 1 --config max.message.bytes=10485760
  bin/kafka-topics.sh --zookeeper 127.0.0.1:2181 --create --topic eastmoney --partitions 4  --replication-factor 1 --config max.message.bytes=10485760
  bin/kafka-topics.sh --zookeeper 127.0.0.1:2181 --create --topic fgw-country --partitions 8  --replication-factor 1 --config max.message.bytes=10485760
  bin/kafka-topics.sh --zookeeper 127.0.0.1:2181 --create --topic paiwuxukezheng --partitions 4  --replication-factor 1 --config max.message.bytes=10485760
  bin/kafka-topics.sh --zookeeper 127.0.0.1:2181 --create --topic ppp --partitions 4  --replication-factor 1 --config max.message.bytes=10485760
  bin/kafka-topics.sh --zookeeper 127.0.0.1:2181 --create --topic province --partitions 8  --replication-factor 1 --config max.message.bytes=10485760
  bin/kafka-topics.sh --zookeeper 127.0.0.1:2181 --create --topic central-enterprise --partitions 8  --replication-factor 1 --config max.message.bytes=10485760
  bin/kafka-topics.sh --zookeeper 127.0.0.1:2181 --create --topic central-enterprise-list --partitions 8  --replication-factor 1 --config max.message.bytes=10485760
  bin/kafka-topics.sh --zookeeper 127.0.0.1:2181 --create --topic policy-list --partitions 8  --replication-factor 1 --config max.message.bytes=10485760
  bin/kafka-topics.sh --zookeeper 127.0.0.1:2181 --create --topic policy --partitions 8  --replication-factor 1 --config max.message.bytes=10485760
  
  ```
  ```
  bin/kafka-topics.sh --zookeeper 127.0.0.1:2181 --create --topic province-disaster --partitions 1  --replication-factor 1 --config max.message.bytes=10485760 --config retention.ms=2592000000
  ```
  参数说明
    + message.max.bytes——>可以接受数据生产者最大消息数据大小
    + retention.ms topic保存时间的毫秒数(一天是86400000毫秒)
    + pykafka的生产者设置参数topic.get_sync_producer(max_request_size=1024 * 1024 * 10)
    + pykafka的消费者设置参数topic.get_simple_consumer(fetch_message_max_bytes=1024 * 1024 * 10)
    + 压缩参数, 需要在生产者加入
      ```shell
      """
        compression:    NONE = 0
                        GZIP = 1
                        SNAPPY = 2
      """
      topic.get_sync_producer(max_request_size=1024 * 1024 * 10,compression=3)
      ```
      用lz4压缩, 需要在kafka所在的机子安装lz4和xxhash,
      ```shell
      yum install lz4-devel -y
      yum install xxhash-devel -y
      ```
      python生产者和消费者端需要安装lz和xxhash库
      ```
      pip install lz4
      pip install xxhash
      ```
      参考: [“Libraries for lz4 compression codec not found”的解决办法](https://blog.csdn.net/yiifaa/article/details/81876338)

+ 删除topic
  ```
  bin/kafka-topics.sh --delete --zookeeper 127.0.0.1:2181 --topic  xxx
  ```

+ 查看topic
  ```
  bin/kafka-topics.sh --describe --zookeeper 127.0.0.1:2181 --topic ppp
  ```

+ 修改topic
  ```
  bin/kafka-topics.sh --zookeeper 127.0.0.1:2181 -alter --topic ppp --partitions 4  --config max.message.bytes=10485760
  ```

+ 查看某个消费者组消费的情况

  ```
  ./bin/kafka-consumer-groups.sh --bootstrap-server 172.24.42.191:9092 --describe --group province_ccgp_group_consumer-5
  ```

  

kafka要求

```
shadowinlife 宫勐:
Kafka容量打到350G，消息存活期72小时

shadowinlife 宫勐:
打到400G吧

shadowinlife 宫勐:
剩下100G可以放日志什么的

shadowinlife 宫勐:
Topic里的partition 打到1.5倍于生产者数量

shadowinlife 宫勐:
像ggzy我们有4个生产者  打6个进去

shadowinlife 宫勐:
备份打到0  单点不用备份

shadowinlife 宫勐:
好像资源不足  partition 个produce 1比1吧

shadowinlife 宫勐:
kakfa消费者逻辑加exception

shadowinlife 宫勐:
当失败后把这个任务写入到特殊的topic

shadowinlife 宫勐:
只有一个partition暂时

信长华:
ok

shadowinlife 宫勐:
ccgp_disaster

shadowinlife 宫勐:
ggzy_disaster

信长华:
我去创建

shadowinlife 宫勐:
这些灾难队列里保存的是对应的三次retry无法处理的任务
```