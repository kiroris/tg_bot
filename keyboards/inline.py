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

# Main_Menu
def main_menu() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(
        text="ACTIONS-1", 
        callback_data="ACTIONS-1")
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
            callback_data='go_to_main_menu'
            )
        )
    return builder.as_markup()

def back_to_information() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text='🔙 Назад',
            callback_data='back_to_information'
            )
        )
    return builder.as_markup()


def delete() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text='💢 Закрыть',
            callback_data='delete'
            )
        )
    return builder.as_markup()

