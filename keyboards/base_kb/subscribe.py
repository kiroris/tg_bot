from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
from config import Config



# Subscribe
def subscribe() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="Подпишись",
        url=Config.link_channel,
        )
    )
    return builder.as_markup()
