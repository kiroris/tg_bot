from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
from dotenv import dotenv_values

config = dotenv_values()

# Main_Menu
def main_menu() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(
        text="Профиль", 
        callback_data="profile")
    )
    builder.row(InlineKeyboardButton(
        text="Профиль",
        callback_data="profile")
    )
    builder.row(
        InlineKeyboardButton(
            text="🌍 Cтраны",
            callback_data="country"
            ),
        InlineKeyboardButton(
            text="HUINYA",
            callback_data="xd"
            )
    )
    # Support Section
    builder.row(
        InlineKeyboardButton(
            text="🏖 Информация",
            callback_data='info'
            ),
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
