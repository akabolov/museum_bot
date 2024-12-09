from aiogram import Router, F
from aiogram.types import Message
from repository.db import Database

router = Router()

@router.message(F.location)
async def text_dummy(message: Message):
    await message.answer('<u>Скоро заработает</u>')
