# MISCONF Redis is configured to save RDB snapshots

### 1.解决方案1: 停止保存快照

```
redis-cli
config set stop-writes-on-bgsave-error no
```

> [参考](https://stackoverflow.com/questions/19581059/misconf-redis-is-configured-to-save-rdb-snapshots)

