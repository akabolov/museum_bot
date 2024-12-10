from aiogram import Router, F
from aiogram.types import Message
from repository.db import Database
from openai_service.openai import get_text_chat

router = Router()

@router.message(F.text)
async def text_dummy(message: Message):
    # TODO: refactor to service
    db = Database()
    await db.store_prompt(message.text, str(message.from_user.id))
    chat = get_text_chat(message.text)
    await message.answer(chat.choices[0].message.content)