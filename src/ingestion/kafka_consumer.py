from confluent_kafka import Consumer
import json

consumer = Consumer({
    "bootstrap.servers": "localhost:9092",
    "group.id": "ecommerce-consumer-group",
    "auto.offset.reset": "earliest"
})

consumer.subscribe(["orders"])

print("Waiting for orders...")

while True:
    message = consumer.poll(1.0)

    if message is None:
        continue

    if message.error():
        print("Consumer error:", message.error())
        continue

    order = json.loads(message.value().decode("utf-8"))

    print("Received order:", order)