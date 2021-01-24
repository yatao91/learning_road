# 使用官方python镜像作为父镜像
FROM python:3.6-alpine

# 指定工作目录
WORKDIR /app

# 复制当前目录内容至容器的`/celery_app`路径
COPY . /app

# 安装项目依赖
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# 开放80端口
EXPOSE 80

# 定义环境变量
ENV NAME world

# 运行app.py
CMD ["python", "app.py"]
