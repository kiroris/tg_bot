from aiogram.types import CallbackQuery, Message
from dotenv import dotenv_values
from run import bot

from keyboards.base_kb.subscribe import subscribe

config = dotenv_values()

async def check_subscription(data):
    if isinstance(data, Message):
        return await message_check_subscription(data)
    elif isinstance(data, CallbackQuery):
        return await callback_check_subscription(data)
    else:
        # Обработка других типов данных, если необходимо
        return False

async def message_check_subscription(message):
    # Ваш код проверки подписки для сообщения
    # Возвращаем id или другой результат
    return message.from_user.id

async def callback_check_subscription(callback):
    # Ваш код проверки подписки для коллбэка
    # Возвращаем id или другой результат
    return callback.from_user.id
