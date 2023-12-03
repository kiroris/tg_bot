from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


def profile_menu() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text="ACTION-1", 
            callback_data="nothink"),
        InlineKeyboardButton(
            text='ACTION-2',
            callback_data='nothink'
            )
    )
    builder.row(
        InlineKeyboardButton(
            text='🔙 Назад',
            callback_data='back_to_main_menu'
            )
        )
    return builder.as_markup()
