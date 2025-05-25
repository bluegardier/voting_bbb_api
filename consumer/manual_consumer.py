from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "votes",
    bootstrap_servers="kafka:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="test-manual",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("Consuming messages...")
for msg in consumer:
    print(f"Received: {msg.value}")