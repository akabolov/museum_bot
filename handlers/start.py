from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from keyboards.menu_question import get_menu_kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    menu_kb = get_menu_kb()
    await message.answer('Привет! 🙋🏼‍♀️\n\n'
                         'Я расскажу, что вокруг тебя есть интересного.'
                         'Ещё ты можешь спросить меня про достопримечательности, и я обсужу их с тобой.\n\n'
                         'Для работы воспользуйся меню:', reply_markup=menu_kb)