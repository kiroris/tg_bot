from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
from dotenv import dotenv_values

config = dotenv_values()


# Subscribe
def subscribe() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="Подпишись",
        url=config['CHANNEL_LINK'],
        )
    )
    return builder.as_markup()
