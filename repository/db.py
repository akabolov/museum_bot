from pymongo import AsyncMongoClient, ASCENDING
from config.values import DB_NAME, DB_URI
from typing import Optional


class Database:
    prompt_collection = "prompts"
    def __init__(self, mongo_uri: str = "mongodb://localhost:27017/"):
        self.client = AsyncMongoClient(mongo_uri)
        self.db = self.client[DB_NAME]

    async def init_db(self):
        collection_names = await self.db.list_collection_names()
        if self.prompt_collection not in collection_names:
            await self.db.create_collection(self.prompt_collection)


        # Add some initial data if the collection is empty
        doc_count = await self.db[self.prompt_collection].count_documents({})
        if doc_count == 0:
            await self.db[self.prompt_collection].insert_many([
                {
                    "prompt": "test",
                    "user_id": "test",
                }
            ])