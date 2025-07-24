# src/api/MessageController.py

from fastapi import APIRouter, HTTPException
from typing import List
from application.Message.dtos.MessageDto import MessageDto
from domain.entities.MessageEntity import MessageEntity
from infrastructure.repositories.MessageRepository import MessageRepository
from application.Message.commands.CreateMessageCommand import CreateMessageCommand
from application.Message.commands.UpdateMessageCommand import UpdateMessageCommand
from application.Message.commands.DeleteMessageCommand import DeleteMessageCommand
from application.Message.queries.GetAllMessagesQuery import GetAllMessagesQuery
from application.Message.queries.GetMessageByIdQuery import GetMessageByIdQuery
from bson import ObjectId
from loguru import logger

router = APIRouter(prefix="/messages", tags=["Messages"])
repository = MessageRepository()

@router.post("/", response_model=str)
def Create(dto: MessageDto):
    command = CreateMessageCommand(repository)
    message_id = command.Handle(dto)
    logger.info("Ação: POST /messages - Mensagem criada | Id: {} | De: {} | Para: {}", message_id, dto.Sender, dto.Recipient)
    return message_id

@router.get("/", response_model=List[MessageEntity])
def GetAll():
    query = GetAllMessagesQuery(repository)
    result = query.Handle()
    logger.info("Ação: GET /messages - {} mensagens retornadas", len(result))
    for item in result:
        item["_id"] = str(item["_id"])
    return result

@router.get("/{id}", response_model=MessageEntity)
def GetById(id: str):
    query = GetMessageByIdQuery(repository)
    result = query.Handle(id)
    if not result:
        logger.warning("Ação: GET /messages/{} - Mensagem não encontrada", id)
        raise HTTPException(status_code=404, detail="Mensagem não encontrada")
    result["_id"] = str(result["_id"])
    logger.info("Ação: GET /messages/{} - Mensagem retornada com sucesso", id)
    return result

@router.put("/{id}")
def Update(id: str, dto: MessageDto):
    command = UpdateMessageCommand(repository)
    command.Handle(id, dto)
    logger.info("Ação: PUT /messages/{} - Mensagem atualizada | De: {} | Para: {}", id, dto.Sender, dto.Recipient)
    return {"message": "Mensagem atualizada com sucesso."}

@router.delete("/{id}")
def Delete(id: str):
    command = DeleteMessageCommand(repository)
    deleted = command.Handle(id)
    if not deleted:
        logger.warning("Ação: DELETE /messages/{} - Mensagem não encontrada", id)
        raise HTTPException(status_code=404, detail="Mensagem não encontrada")
    logger.info("Ação: DELETE /messages/{} - Mensagem deletada com sucesso", id)
    return {"message": "Mensagem excluída com sucesso."}
