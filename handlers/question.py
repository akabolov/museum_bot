from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from repository.db import Database
from keyboards.menu_question import menu_buttons

router = Router()

@router.message(F.text==menu_buttons.get('question'))
async def user_question(message: Message):
    await message.answer("Задай мне вопрос о достопримечательности, "
                         "и я на него отвечу 😉", reply_markup=ReplyKeyboardRemove())
    