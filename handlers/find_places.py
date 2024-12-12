from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from repository.db import Database
from keyboards.menu_question import menu_buttons

router = Router()

@router.message(F.text==menu_buttons.get('find_places'))
async def find_places(message: Message):
    await message.answer("Отправь мне текущую локацию, "
                         "чтобы найти интересные места неподалеку", reply_markup=ReplyKeyboardRemove())
