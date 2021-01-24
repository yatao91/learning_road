# 使用centos作为基础镜像
FROM centos

# 指明dockerfile维护者
LABEL maintainer="suyatao"

# 安装memcached
RUN yum install -y memcached

# 开放端口:11211(memcache默认端口:11211)
EXPOSE 11211

# 设置运行memcached守护进程的用户
USER daemon

# 设置memcached可执行文件入口
ENTRYPOINT memcached

# memcached默认运行命令参数
CMD ["-m", "128"]