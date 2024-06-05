from abc import ABC, abstractmethod

from motor.motor_asyncio import AsyncIOMotorClient

from src.config import settings

client = AsyncIOMotorClient(
    settings.database_url, uuidRepresentation="standard", minPoolSize=12, maxPoolSize=16
)
db = client[settings.db_name]


class AbstractRepository(ABC):
    @abstractmethod
    async def add(self, entity_id):
        raise NotImplementedError

    @abstractmethod
    async def get(self, entity_id):
        raise NotImplementedError


class HistoryRepository(AbstractRepository):
    def __init__(self):
        self.collection = db.get_collection("histories")

    async def add(self, chat_id):
        entity = {}
        entity["_id"] = chat_id
        entity["history"] = []

        result = await self.collection.insert_one(entity)
        return result

    async def get(self, chat_id):
        document = await self.collection.find_one({"_id": chat_id})
        return document

    async def delete(self, chat_id):
        await self.collection.delete_one({"_id": chat_id})

    async def add_message(self, chat_id, message):
        await self.collection.update_one(
            {"_id": chat_id},
            {"$push": {"history": message}},
        )

    async def clear_history(self, chat_id):
        await self.collection.update_one(
            {"_id": chat_id},
            {
                "$unset": {
                    field: "" for field in await self.get_fields_to_unset(chat_id)
                },
            },
        )

        await self.collection.update_one(
            {"_id": chat_id},
            {"$set": {"history": []}},
        )

    async def get_fields_to_unset(self, chat_id):
        # Retrieve the document to clean
        document = await self.collection.find_one({"_id": chat_id})
        if document:
            # Create a list of all fields to unset, excluding '_id'
            fields_to_unset = [field for field in document if field != "_id"]
            return fields_to_unset
        return []
