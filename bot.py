from config.values import BOT_TOKEN, DB_URI
from repository.db import Database

def test_db():
    db = Database(DB_URI)
    print(db.db.list_collection_names())
    print(db.db[db.prompt_collection].count_documents({}))
    print(db.db[db.prompt_collection].find_one())

print(BOT_TOKEN)
test_db()