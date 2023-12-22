from aiogram.types import CallbackQuery, Message
from dotenv import dotenv_values
from run import bot

from keyboards.base_kb.subscribe import subscribe

config = dotenv_values()

async def get_user_id(data):
    if isinstance(data, Message):
        return await message_get_id(data)
    elif isinstance(data, CallbackQuery):
        return await callback_get_id(data)
    else:
        # Обработка других типов данных, если необходимо
        return False

async def message_get_id(message: Message):
    # Ваш код проверки подписки для сообщения
    # Возвращаем id или другой результат
    return message.from_user.id

async def callback_get_id(callback_query: CallbackQuery):
    # Ваш код проверки подписки для коллбэка
    # Возвращаем id или другой результат
    return callback.from_user.id
