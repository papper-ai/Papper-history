from motor.motor_asyncio import AsyncIOMotorClient


class MongoDBClient:
    def __init__(self, db_name, collection_name):
        self.client = AsyncIOMotorClient('mongodb://localhost:27017/')
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    async def insert_document(self, document):
        return await self.collection.insert_one(document)

    async def delete_document(self, chat_id):
        return await self.collection.delete_one({"chat_id": chat_id})
