from typing import Optional
from pymongo import AsyncMongoClient

from config.values import DB_NAME, DB_URI


class Database:
    _instance: Optional['Database'] = None
    _initialized: bool = False
    prompt_collection = "prompts"

    def __new__(cls, mongo_uri: str = DB_URI) -> 'Database':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, mongo_uri: str = DB_URI):
        if not Database._initialized:
            self.client = AsyncMongoClient(mongo_uri)
            self.db = self.client[DB_NAME]
            Database._initialized = True

    async def store_prompt(self, prompt: str, user_id: str):
        await self.db[self.prompt_collection].insert_one({
            "prompt": prompt,
            "user_id": user_id,
        })

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