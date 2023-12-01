from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
from config import Config

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
            url=Config.support_live,
            )
        )
    builder.row(
        InlineKeyboardButton(
            text='Справка по боту',
            url='kiroris.github.io'
            )
        )
    return builder.as_markup()
