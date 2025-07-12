# src/infrastructure/messaging/KafkaSubscriber.py

import json
from kafka import KafkaConsumer
from core.Config import GetSettings

settings = GetSettings()

class KafkaSubscriber:
    def __init__(self):
        self.topic = settings.KAFKA_TOPIC
        self.consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
            group_id=settings.KAFKA_GROUP_ID,
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            value_deserializer=lambda m: json.loads(m.decode("utf-8"))
        )

    def listen(self):
        print(f"Aguardando mensagens Kafka no tópico '{self.topic}'...")
        for message in self.consumer:
            print(f"[KAFKA - {self.topic}] Mensagem recebida:", message.value)


# Execução direta (modo CLI)
if __name__ == "__main__":
    KafkaSubscriber().listen()


# Execução via FastAPI (async background)
def start_kafka_subscriber():
    KafkaSubscriber().listen()


