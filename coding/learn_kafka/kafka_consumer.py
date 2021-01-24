import time
import json

from confluent_kafka import Consumer, KafkaError


def commit_cb(err, ps):
    print("on_commit: err %s, partitions %s" % (err, ps))


KAFKA_HOST = "192.168.138.191:9092"
KAFKA_CONSUMER_ID = "important-topic"
c = Consumer(
    {
        "bootstrap.servers": KAFKA_HOST,
        "group.id": KAFKA_CONSUMER_ID,
        "default.topic.config": {"auto.offset.reset": "earliest"},
        "enable.auto.commit": False
    }
)

start_time = time.time()

c.subscribe(["important-topic-huatai"])

while True:

    message = c.poll(1.0)

    if not message:
        print(1)
        continue

    if message.error():
        if message.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            break

    raw_data = message.value().decode()

    raw_key = message.key()
    if raw_key:
        key = raw_key.decode()
    else:
        key = ""
    try:
        print(key, json.loads(raw_data), message.partition(), message.offset())

    except Exception as e:
        print(e)
    finally:
        c.commit()
