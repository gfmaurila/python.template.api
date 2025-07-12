# src/infrastructure/messaging/RabbitMQPublisher.py

import json
import pika
from core.Config import GetSettings

settings = GetSettings()

class RabbitMQPublisher:
    def __init__(self):
        self.exchange = settings.RABBITMQ_EXCHANGE
        credentials = pika.PlainCredentials(settings.RABBITMQ_USER, settings.RABBITMQ_PASSWORD)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=settings.RABBITMQ_HOST,
            port=settings.RABBITMQ_PORT,
            credentials=credentials
        ))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(
            exchange=self.exchange,
            exchange_type='fanout',
            durable=True
        )

    def publish(self, message: dict):
        payload = json.dumps(message)
        self.channel.basic_publish(
            exchange=self.exchange,
            routing_key='',
            body=payload
        )
        print(f"[RABBITMQ] Publicado em '{self.exchange}': {payload}")
