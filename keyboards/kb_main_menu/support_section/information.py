from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
from config import Config

def information() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text="📚 Правила", 
            callback_data="rules"),
        InlineKeyboardButton(
            text='🆘 Поддержка',
            callback_data='support'
            )
    )
    builder.row(
        InlineKeyboardButton(
            text='🔙 Назад',
            callback_data='back_to_main_menu'
            )
        )
    return builder.as_markup()
