from fastapi import APIRouter
from infrastructure.messaging.User.Pub.RedisPublisher import RedisPublisher
from infrastructure.messaging.User.Pub.RabbitMQPublisher import RabbitMQPublisher
from infrastructure.messaging.User.Pub.KafkaPublisher import KafkaPublisher
from loguru import logger

router = APIRouter(prefix="/test-messaging", tags=["Messaging Test"])

sample_payload = {
    "Id": 999,
    "Name": "Fulano",
    "Email": "fulano@teste.com.br",
    "Phone": "(51) 985623314",
    "Notification": "Notification via email",
    "Gender": "Male"
}

@router.post("/redis")
async def test_redis():
    RedisPublisher().publish("user-created", sample_payload)
    logger.info("Ação: POST /test-messaging/redis - Mensagem publicada no canal 'user-created' via Redis | Payload: {}", sample_payload)
    return {"message": "Mensagem publicada no Redis"}

@router.post("/rabbitmq")
async def test_rabbitmq():
    RabbitMQPublisher().publish(sample_payload)
    logger.info("Ação: POST /test-messaging/rabbitmq - Mensagem publicada via RabbitMQ | Payload: {}", sample_payload)
    return {"message": "Mensagem publicada no RabbitMQ"}

@router.post("/kafka")
async def test_kafka():
    KafkaPublisher().publish(sample_payload)
    logger.info("Ação: POST /test-messaging/kafka - Mensagem publicada via Kafka | Payload: {}", sample_payload)
    return {"message": "Mensagem publicada no Kafka"}
