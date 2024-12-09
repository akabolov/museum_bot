from config.values import BOT_TOKEN, DB_URI
from repository.db import Database
import asyncio

async def test_db():
    db = Database(DB_URI)
    await db.init_db()
    print(await db.db.list_collection_names())
    print(await db.db[db.prompt_collection].count_documents({}))
    print(await db.db[db.prompt_collection].find_one())

print(BOT_TOKEN)

loop = asyncio.get_event_loop()
loop.run_until_complete(test_db())