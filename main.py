import asyncio
from bot.create_bot import bot, dp
from handlers import start, text, location, question, about, find_places


async def main():
    dp.include_routers(start.router, about.router, find_places.router, question.router, text.router, location.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
