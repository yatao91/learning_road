# -*- coding: utf-8 -*-
from celery.schedules import crontab

result_serializer = 'json'

# broker设置
broker_url = "redis://{}:{}/0".format('127.0.0.1', '6380')

# 存储任务状态和结果的存储后端
result_backend = "redis://{}:{}/1".format('127.0.0.1', '6380')

# 时区
timezone = "Asia/Shanghai"

imports = [
    "celery_app.tasks"
]

# 需要执行任务的配置
beat_schedule = {
    "test1": {
        "task": "celery_app.tasks.test1",  #执行的函数
        "schedule": crontab(minute="*/1"),   # every minute 每分钟执行
        "args": ()  # # 任务函数参数
    }
}
