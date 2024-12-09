from pymongo import MongoClient, ASCENDING
from config.values import DB_NAME, DB_URI
from typing import Optional


class Database:
    prompt_collection = "prompts"
    def __init__(self, mongo_uri: str = "mongodb://localhost:27017/"):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[DB_NAME]
        self.init_db()

    def init_db(self):
        if self.prompt_collection not in self.db.list_collection_names():
            self.db.create_collection(self.prompt_collection)


        # Add some initial data if the collection is empty
        if self.db[self.prompt_collection].count_documents({}) == 0:
            self.db[self.prompt_collection].insert_many([
                {
                    "prompt": "test",
                    "user_id": "test",
                }
            ])