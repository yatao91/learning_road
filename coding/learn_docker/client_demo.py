# -*- coding: utf-8 -*-
import docker

# 使用默认的socket连接docker服务
# client = docker.from_env()

client = docker.DockerClient(base_url='tcp://127.0.0.1:2375')

# 指定运行容器
# resp = client.containers.run('hello-world')

# 后台运行container
# resp = client.containers.run('hello-world', detach=True)
#
# print(resp)

# 获取容器列表
container_list = client.containers.list()

print(container_list)
print("-"*30)

# 获取容器
container = client.containers.get('5cbe57a9a7')

print(container)
print("-"*30)
print(dir(container))
print("-"*30)
print(container.attrs)
print("-"*30)
print(container.attrs['Config']['Image'])
print("-"*30)
print(container.logs(tail=20))

# 停止容器
# container.stop()

print("-"*30)

# 流式输出日志
# for line in container.logs(stream=True):
#     print(line.strip())

# 拉取镜像
# resp = client.images.pull('nginx')
# print(resp)

# 获取镜像列表
image_list = client.images.list()
print(image_list)
