+ 准备工作
  + es官网下载6.40的es压缩包, 并解压.  https://www.elastic.co/downloads/past-releases
  + jieba es插件的github上下载相应版本的源码,  用有gradle的机子编译成es插件, 并将插件scp到es的plugins目录中.  https://github.com/sing1ee/elasticsearch-jieba-plugin
  + centos安装openjdk8, 参考 https://blog.csdn.net/youzhouliu/article/details/51183115

+ 修改centos系统的配置,  符合es的启动要求
  + 防止出现`max file descriptors [4096] for elasticsearch process is too low, increase to at least [65536]`, 需要修改

    ```
    编辑 /etc/security/limits.conf
    在文件最后添加, 不要忘记星号
    * soft nofile 65536
    * hard nofile 65536
    保存后重启centos
    ```

  + 防止出现`max virtual memory areas vm.max_map_count [65530] is too low, increase to at least [262144]`, 需要修改

    ```
    su 
    echo "vm.max_map_count=262144" > /etc/sysctl.conf
    sysctl -p
    ```

+ 修改es的配置文件`config/elasticsearch.yml`, 3台机子 默认都是master节点 都是data节点

  ```
  cluster.name: jiefeng_es
  node.name: jiefeng_es01
  path.data: /data/es_data
  path.logs: /data/es_logs
  network.host: 10.0.1.4 # 本机内网ip地址,
  http.port: 9288
  discovery.zen.ping.unicast.hosts: ["10.0.1.4", "10.0.1.5", "10.0.1.6"]
  ```

+ 修改es的jvm配置文件`config/jvm.options`

  ```
  -Xms6g 初始内存值,  机子配置的内存是8g, 给es分配6g
  -Xmx6g 最大内存值
  -Xss100m
  
  ```

+ 设置完成后, 3台机子分别启动es, 并根据显示在屏幕上的启动日志检查是否有错误

  ```
  bin/elasticsearch
  ```

+ 浏览器访问相应的ip和端口, 查看es插件 节点 分配内存等信息是否正确

  ```
  10.0.1.4:9288/nodes
  ```

+ 用后台启动命令重新启动es

  ```
  bin/elasticsearch -d
  ```

  





