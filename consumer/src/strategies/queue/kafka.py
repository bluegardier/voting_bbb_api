from kafka import KafkaConsumer
import json
from src.strategies.queue.base import QueueStrategy
from src.logger import default_logger


class KafkaQueue(QueueStrategy):
    def __init__(self, settings):
        default_logger.info(f"KafkaQueue init with topic={settings.kafka_topic}, bootstrap_servers={settings.kafka_bootstrap_servers}")
        self.topic = settings.kafka_topic
        self.bootstrap_servers = settings.kafka_bootstrap_servers
        self.consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=self.bootstrap_servers,
            value_deserializer=lambda m: json.loads(m.decode("utf-8")),
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            group_id="voting-consumer-group",
        )

    def consume(self):
        default_logger.info("Starting consumption loop")
        for message in self.consumer:
            default_logger.info(f"Message received from Kafka: {message.value}")
            yield message.value
