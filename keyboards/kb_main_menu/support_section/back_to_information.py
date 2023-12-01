from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

def back_to_information() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text='🔙 Назад',
            callback_data='back_to_information'
            )
        )
    return builder.as_markup()
