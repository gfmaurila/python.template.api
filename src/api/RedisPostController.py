# src/api/RedisPostController.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from uuid import uuid4
from typing import List
import json
import redis.asyncio as redis

from core.Config import GetSettings

router = APIRouter(prefix="/redis-posts", tags=["RedisPosts"])

# Configuração padrão via settings
settings = GetSettings()
redisUrl = f"redis://:{settings.REDIS_PASSWORD}@{settings.REDIS_HOST}:{settings.REDIS_PORT}/3"
RedisClient = redis.from_url(redisUrl, decode_responses=True)


# Padrão de classe estilo C#
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
    return posts


@router.get("/{id}", response_model=RedisPostModel)
async def GetById(id: str):
    data = await RedisClient.get(f"RedisPost:{id}")
    if not data:
        raise HTTPException(status_code=404, detail="Post not found")
    return RedisPostModel(**json.loads(data))


@router.post("/", response_model=RedisPostModel)
async def Create(post: RedisPostModel):
    post.Id = str(uuid4())
    await RedisClient.set(f"RedisPost:{post.Id}", post.model_dump_json())
    return post


@router.put("/{id}", response_model=RedisPostModel)
async def Update(id: str, post: RedisPostModel):
    exists = await RedisClient.get(f"RedisPost:{id}")
    if not exists:
        raise HTTPException(status_code=404, detail="Post not found")
    post.Id = id
    await RedisClient.set(f"RedisPost:{id}", post.model_dump_json())
    return post


@router.delete("/{id}")
async def Delete(id: str):
    deleted = await RedisClient.delete(f"RedisPost:{id}")
    if deleted == 0:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": f"Post {id} deleted successfully"}
