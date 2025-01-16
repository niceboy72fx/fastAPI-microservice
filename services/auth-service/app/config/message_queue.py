from confluent_kafka import Consumer, KafkaException
from typing import Callable

class ProducerQueue:
    def __init__(self, config: dict):
        self.config = config
        self.producer = Producer(self.config)

    def invoke_message(self, err, message):
        pass

    def on_message(self, topic: str, key: str, value: str, callback: Callable = None):
        pass

class ConsumerQueue:
    def __init__(self, bootstrap_servers: str, topics: List[str], config: dict):
        self.config = config
        self.producer = Producer(self.config)

    def on_message(self, topic: str, key: str, value: str, callback: Callable = None, time_out: float):
        self.consumer.subscribe(self.topics)
        try:
            while True:
                msg = self.consumer.poll(time_out)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaException._PARTITION_EOF:
                        print(f"End of partition reached {msg.topic()} [{msg.partition()}]")
                    else:
                        print(f"Error: {msg.error()}")
                        break
                else:
                    print(f"Received message: {msg.value().decode('utf-8')} from {msg.topic()} [{msg.partition()}]")
        except KeyboardInterrupt:
            print("Consumer interrupted")
        finally:
            self.consumer.close()