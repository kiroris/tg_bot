from aiogram.utils.keyboard import ReplyKeyboardBuilder

def menu() -> ReplyKeyboardBuilder:
    kb = ReplyKeyboardBuilder()
    kb.button(text="✉️ Меню")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
