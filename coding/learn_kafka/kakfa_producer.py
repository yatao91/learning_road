import json

from kafka import KafkaProducer

KAFKA_HOST = ["192.168.138.191:9092"]


class KafkaDriver:

    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=KAFKA_HOST,
            retries=5,
            api_version=(0, 10),
            max_request_size=1024 * 1024 * 30,
            compression_type="lz4",
        )

    def produce(self, topic_name, item):

        if isinstance(item, dict):
            item = json.dumps(item)

        for i in range(3):
            try:
                future = self.producer.send(topic_name, value=item.encode())
                result = future.get(timeout=10)
                return result
            except Exception as e:
                self.close()
                self.__init__()
                if i == 2:
                    raise e

    def produce_kill_signal(self, topic_name, partition_num):

        for p in range(partition_num):
            future = self.producer.send(topic=topic_name, key="kill".encode(), partition=p, value='kill'.encode())
            ret = future.get()
            print(topic_name, ret.partition, ret.offset)

        self.producer.flush()
        return

    def close(self):
        self.producer.close()


if __name__ == "__main__":
    kafka_driver = KafkaDriver()

    topic_import = False

    if topic_import:
        for i in range(1, 1010):
            ret = kafka_driver.produce(topic_name="important-topic", item={"data": i})
            print(ret.partition, ret.offset)

        kafka_driver.produce_kill_signal(topic_name='important-topic', partition_num=6)

    else:
        for i in range(1, 1010):
            ret = kafka_driver.produce(topic_name="normal-topic", item={"data": i})
            print(ret.partition, ret.offset)
