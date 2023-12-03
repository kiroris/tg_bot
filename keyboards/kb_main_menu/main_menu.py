from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
from dotenv import dotenv_values

config = dotenv_values()

# Main_Menu
def main_menu() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(
        text="Профиль", 
        callback_data="personal_account")
    )
    builder.row(InlineKeyboardButton(
        text="ACTIONS-2",
        callback_data="ACTIONS-2")
    )
    builder.row(
        InlineKeyboardButton(
            text="🏖 Информация",
            callback_data='info'),
        InlineKeyboardButton(
            text='🆘 Поддержка',
            url=config['SUPPORT_ADMIN'],
            )
        )
    builder.row(
        InlineKeyboardButton(
            text='Справка по боту',
            url=config['SUPPORT_SITE']
            )
        )
    return builder.as_markup()
