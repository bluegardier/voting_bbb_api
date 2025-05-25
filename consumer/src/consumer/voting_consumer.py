from kafka import KafkaConsumer
import json
from typing import Any
import time


def run_consumer(settings: Any, db_strategy: Any):
    consumer = KafkaConsumer(
        settings.kafka_topic,
        bootstrap_servers=settings.kafka_bootstrap_servers,
        value_deserializer=lambda m: json.loads(m.decode("utf-8")),
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="voting-consumer-group-test",
    )

    buffer = []
    last_flush_time = time.time()

    for message in consumer:
        buffer.append(message.value)

        if len(buffer) >= 1000 or (time.time() - last_flush_time) >= 180:
            for vote in buffer:
                try:
                    db_strategy.insert_vote(vote)
                except Exception as e:
                    print(f"Failed to insert vote: {e}")
            buffer.clear()
            last_flush_time = time.time()
