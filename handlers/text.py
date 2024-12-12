from aiogram import Router, F
from aiogram.types import Message
from repository.db import Database
from openai_service.openai import get_text_chat
from keyboards.menu_question import get_menu_kb

router = Router()

@router.message(F.text)
async def text_dummy(message: Message):
    menu_kb = get_menu_kb()
    db = Database()
    await db.store_prompt(message.text, str(message.from_user.id))
    chat = get_text_chat(message.text)
    await message.answer(chat.choices[0].message.content, 
                         reply_markup=menu_kb)