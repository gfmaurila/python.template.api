# src/infrastructure/messaging/KafkaPublisher.py

import json
from kafka import KafkaProducer
from core.Config import GetSettings

settings = GetSettings()

class KafkaPublisher:
    def __init__(self):
        self.topic = settings.KAFKA_TOPIC
        self.producer = KafkaProducer(
            bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )

    def publish(self, message: dict):
        self.producer.send(self.topic, message)
        self.producer.flush()
        print(f"[KAFKA] Publicado no tópico '{self.topic}': {message}")

