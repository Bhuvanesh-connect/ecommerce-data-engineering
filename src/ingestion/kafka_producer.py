from confluent_kafka import Producer
import json

producer = Producer({
    "bootstrap.servers": "localhost:9092"
})

order = {
    "order_id": 1004,
    "customer_id": "C001",
    "product_id": "P101",
    "quantity": 1,
    "price": 60000
}

producer.produce(
    "orders",
    value=json.dumps(order)
)

producer.flush()

print("Order sent to Kafka")