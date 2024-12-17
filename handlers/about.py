from aiogram import Router, F
from aiogram.types import Message
from repository.db import Database
from openai_service.openai import get_location_chat
from keyboards.menu_question import menu_buttons, get_menu_kb

router = Router()

@router.message(F.text==menu_buttons.get('about'))
async def info_about(message: Message):
    menu_kb = get_menu_kb()
    await message.answer("Здесь мы расскажем о нашем проекте.\n\n"
                         "Воспользуйся меню:", reply_markup=menu_kb)
