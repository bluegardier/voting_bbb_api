from src.strategies.queue.kafka import KafkaQueue
from config import Settings


class QueueFactory:
    @staticmethod
    def create(settings: Settings):
        strategy = settings.queue_strategy.lower()
        if strategy == "kafka":
            return KafkaQueue(settings)
        else:
            raise ValueError(f"Unsupported queue strategy: {strategy}")
