from aiogram import Router, F
from aiogram.types import Message
from repository.db import Database

router = Router()

@router.message(F.text)
async def text_dummy(message: Message):
    # TODO: refactor to service
    db = Database()
    await db.store_prompt(message.text, str(message.from_user.id))
    await message.answer('Отправляю текст в OPENAPI')