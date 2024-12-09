from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('<b>Напиши</b> о чем хочешь спросить или отправь текущую локацию чтобы найти интересные места неподалеку')