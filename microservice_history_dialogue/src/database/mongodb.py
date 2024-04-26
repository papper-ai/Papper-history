from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["chat_history"]
collection = db["dialogs"]


async def insert_document(document):
    return await collection.insert_one(document)


async def delete_document(chat_id):
    return await collection.delete_one({"chat_id": chat_id})
