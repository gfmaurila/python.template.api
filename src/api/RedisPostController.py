# src/api/RedisPostController.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from uuid import uuid4
from typing import List
import json
import redis.asyncio as redis
from loguru import logger

from core.Config import GetSettings

router = APIRouter(prefix="/redis-posts", tags=["RedisPosts"])

settings = GetSettings()
redisUrl = f"redis://:{settings.REDIS_PASSWORD}@{settings.REDIS_HOST}:{settings.REDIS_PORT}/3"
RedisClient = redis.from_url(redisUrl, decode_responses=True)

class RedisPostModel(BaseModel):
    Id: str
    Title: str
    Content: str

@router.get("/", response_model=List[RedisPostModel])
async def GetAll():
    keys = await RedisClient.keys("RedisPost:*")
    posts = []
    for key in keys:
        data = await RedisClient.get(key)
        if data:
            posts.append(RedisPostModel(**json.loads(data)))
    logger.info("Ação: GET /redis-posts - Retornados {} posts", len(posts))
    return posts

@router.get("/{id}", response_model=RedisPostModel)
async def GetById(id: str):
    data = await RedisClient.get(f"RedisPost:{id}")
    if not data:
        logger.warning("Ação: GET /redis-posts/{} - Post não encontrado", id)
        raise HTTPException(status_code=404, detail="Post not found")
    logger.info("Ação: GET /redis-posts/{} - Post retornado com sucesso", id)
    return RedisPostModel(**json.loads(data))

@router.post("/", response_model=RedisPostModel)
async def Create(post: RedisPostModel):
    post.Id = str(uuid4())
    await RedisClient.set(f"RedisPost:{post.Id}", post.model_dump_json())
    logger.info("Ação: POST /redis-posts - Post criado | Id: {} | Título: {}", post.Id, post.Title)
    return post

@router.put("/{id}", response_model=RedisPostModel)
async def Update(id: str, post: RedisPostModel):
    exists = await RedisClient.get(f"RedisPost:{id}")
    if not exists:
        logger.warning("Ação: PUT /redis-posts/{} - Post não encontrado para atualização", id)
        raise HTTPException(status_code=404, detail="Post not found")
    post.Id = id
    await RedisClient.set(f"RedisPost:{id}", post.model_dump_json())
    logger.info("Ação: PUT /redis-posts/{} - Post atualizado | Título: {}", id, post.Title)
    return post

@router.delete("/{id}")
async def Delete(id: str):
    deleted = await RedisClient.delete(f"RedisPost:{id}")
    if deleted == 0:
        logger.warning("Ação: DELETE /redis-posts/{} - Post não encontrado", id)
        raise HTTPException(status_code=404, detail="Post not found")
    logger.info("Ação: DELETE /redis-posts/{} - Post deletado com sucesso", id)
    return {"message": f"Post {id} deleted successfully"}
