from typing import Annotated

from uuid import UUID

from fastapi import APIRouter, Body, status

from schemas import ChatData
from microservice_history_dialogue.src.database.mongodb import delete_document, insert_document
from utils import replace_uuid

hd_router = APIRouter(tags=["Mongo_Base"])


@hd_router.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload(input: Annotated[ChatData, Body(...)]) -> None:
    chat_data = replace_uuid(input.dict())
    await insert_document(chat_data)
    return {"message": "Chat created successfully"}


@hd_router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
async def delete(vault_id: Annotated[UUID, Body(embed=True)]) -> None:
    chat_id_obj = str(vault_id)
    await delete_document(chat_id_obj)

    return {"message": "Chat deleted successfully"}

