# src/infrastructure/messaging/RabbitMQSubscriber.py

import pika
import json
from core.Config import GetSettings

settings = GetSettings()

class RabbitMQSubscriber:
    def __init__(self):
        self.exchange = settings.RABBITMQ_EXCHANGE
        self.queue_name = settings.RABBITMQ_QUEUE

        credentials = pika.PlainCredentials(settings.RABBITMQ_USER, settings.RABBITMQ_PASSWORD)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=settings.RABBITMQ_HOST,
            port=settings.RABBITMQ_PORT,
            credentials=credentials
        ))
        self.channel = self.connection.channel()

        # Declarações
        self.channel.exchange_declare(exchange=self.exchange, exchange_type='fanout', durable=True)
        self.channel.queue_declare(queue=self.queue_name, durable=True)
        self.channel.queue_bind(exchange=self.exchange, queue=self.queue_name)

    def callback(self, ch, method, properties, body):
        data = json.loads(body)
        print(f"[RABBITMQ - {self.queue_name}] Mensagem recebida:", data)

    def listen(self):
        self.channel.basic_consume(
            queue=self.queue_name,
            on_message_callback=self.callback,
            auto_ack=True
        )
        print(f"Aguardando mensagens RabbitMQ na fila '{self.queue_name}' vinculada ao exchange '{self.exchange}'...")
        self.channel.start_consuming()


# Execução direta (CLI)
if __name__ == "__main__":
    subscriber = RabbitMQSubscriber()
    subscriber.listen()


# Execução via FastAPI
def start_rabbitmq_subscriber():
    subscriber = RabbitMQSubscriber()
    subscriber.listen()
