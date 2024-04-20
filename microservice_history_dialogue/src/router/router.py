from schemas import Document, Message
from fastapi import APIRouter, Request
from utils import MongoDBClient
from bson import ObjectId

router = APIRouter(tags=["Mongo Base"])

db_name = "chat_history"
collection_name = "dialogs"

db_client = MongoDBClient(db_name, collection_name)


@router.post('/chats')
async def create_chat(request: Request):
    request_data = await request.json()
    chat = Document(**request_data)
    chat_id = await db_client.insert_document(chat)
    return {"chat_id": str(chat_id)}


@router.delete('/chats/{chat_id}')
async def delete_chat(chat_id: str):
    await db_client.delete_document(ObjectId(chat_id))
    return {"message": "Chat deleted"}
