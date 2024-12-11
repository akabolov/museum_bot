from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Чтобы поменять текст кнопок, замени value в словаре ниже
menu_buttons = {
    'find_places': 'Найти места рядом',
    'question': 'Обсудить достопримечательность',
    'about': 'О проекте'
}

def get_menu_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=menu_buttons.get('find_places'))
    kb.button(text=menu_buttons.get('question'))
    kb.button(text=menu_buttons.get('about'))
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
   
