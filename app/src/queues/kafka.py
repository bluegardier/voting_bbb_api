from .base import QueueService
from typing import Dict
from aiokafka import AIOKafkaProducer
import json

class KafkaQueueService(QueueService):
    def __init__(
        self,
        bootstrap_servers: str = "kafka:9092",
        topic: str = "votes"):
        
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic
        self.producer = None

    async def _get_producer(self):
        if not self.producer:
            self.producer = AIOKafkaProducer(
                bootstrap_servers=self.bootstrap_servers,
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
            await self.producer.start()
        return self.producer

    async def send(self, data: Dict):
        producer = await self._get_producer()
        await producer.send_and_wait(self.topic, data)