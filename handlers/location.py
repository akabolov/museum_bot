from aiogram import Router, F
from aiogram.types import Message
from repository.db import Database
from openai_service.openai import get_location_chat

router = Router()

@router.message(F.location)
async def text_dummy(message: Message):
    chat = get_location_chat(message.location.latitude, message.location.longitude)
    await message.answer(chat.choices[0].message.content)
