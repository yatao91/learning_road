+  普通lua脚本在阿里云redis 集群上运行报错: 'EVALSHA' command keys must in same slot 

  ```
  # ~= lua 中的 !=
      lua = """
          local ret = redis.call("exists", KEYS[1])
          if ret ~= 1
          then
              return ret
          end
          ret = redis.call("hincrby", KEYS[1], KEYS[2], 1)
          return ret
      """
  
      script = redis_driver.register_script(lua)
      script(keys=[key, field])
  ```

+ 改写lua脚本

  ```
      # ~= lua 中的 !=
      lua = """
          local ret = redis.call("exists", KEYS[1])
          if ret ~= 0
          then
              return ret
          end
          ret = redis.call("hincrby", KEYS[1], ARGV[1], 1)
          return ret
      """
  
      script = redis_driver.register_script(lua)
      script(keys=[key], args=[field])
  ```

+  重新设计redis key,  sniffer:{pid}:127.0.1.1:2642 在key的某个单词上前后增加大括号, 保证这个key在一个redis cluster的slot内. 

  +  redis key的样式从 ` sniffer:pid:127.0.1.1:2642` 改成 ` sniffer:{pid}:127.0.1.1:2642`

  + 如果是python 的format语法, 需要这样写

    ```
    pid_key_name = "{}:{{pid}}:{}:{}".format(REDIS_KEY_PREFIX, ip_address, pid)
    ```

    

+ 参考:

  + [redis官网]( https://redis.io/topics/cluster-spec )
  + [阿里云官网说明]( https://tech.antfin.com/docs/2/92942 )
  + [Redis注意事项及常见优化](https://nicky-chen.github.io/2018/08/07/cache-redis-optimize/)
  + [阿里云redis集群使用lua脚本]( https://blog.csdn.net/mushuntaosama/article/details/78788254 )