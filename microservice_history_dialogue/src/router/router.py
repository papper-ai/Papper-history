from typing import Annotated

from uuid import UUID
from bson.objectid import ObjectId

from fastapi import APIRouter, Body, status

from schemas import Chat
from microservice_history_dialogue.src.database.mongodb import MongoDBClient

hd_router = APIRouter(tags=["Mongo Base"])


@hd_router.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload(input: Annotated[Chat, Body(...)]) -> None:
    chat_data = input.dict()

    async def save_chat_in_db():
        collection.insert_one(chat_data)

    return {"message": "Chat created successfully"}


@hd_router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
async def delete(vault_id: Annotated[UUID, Body(embed=True)]) -> None:
    chat_id_obj = ObjectId(vault_id)

    async def delete_chat_from_db():
        collection.delete_one({"chat_id": chat_id_obj})

    return {"message": "Chat deleted successfully"}