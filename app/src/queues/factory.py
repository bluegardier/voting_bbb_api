from .kafka import KafkaQueueService
from .base import QueueService


def get_queue_service(backend: str = "kafka") -> QueueService:
    if backend == "kafka":
        return KafkaQueueService()
    # elif backend == "rabbitmq":
    #     return RabbitMQQueueService()
    # elif backend == "redis":
    #     return RedisQueueService()
    else:
        raise ValueError(f"Unknown queue backend: {backend}")
