from aiogram.types import CallbackQuery, Message
from dotenv import dotenv_values
from run import bot

from keyboards.base_kb.subscribe import subscribe

config = dotenv_values()

need_a_check = True

async def check_subscription(data):
    if need_a_check:
        if isinstance(data, Message):
            return await message_check_subscription(data)
        elif isinstance(data, CallbackQuery):
            return await callback_check_subscription(data)
        else:
            # Обработка других типов данных, если необходимо
            return False
    else:
        return True

#==========CHECK_SUBSCRIPTION(FOR_MESSAGE/COMMAND)==========#
async def message_check_subscription(message: Message):
    chat_member = await bot.get_chat_member(config['CHANNEL_ID'], message.from_user.id)
    if chat_member.status == "member":
        return True
    elif chat_member.status == "administrator" or chat_member.status == "creator":
        return True
    else:
        await bot.send_message(message.chat.id, "Подпишись на канал, чтобы использовать бота", reply_markup=subscribe())
        return False

#==========CHECK_SUBSCRIPTION(FOR_CALLBACK)==========#
async def callback_check_subscription(callback_query: CallbackQuery):
    chat_member = await bot.get_chat_member(config['CHANNEL_ID'], callback_query.from_user.id)
    if chat_member.status == "member":
        return True
    elif chat_member.status == "administrator" or chat_member.status == "creator":
        return True
    else:
        await bot.answer_callback_query(callback_query.id, "Чтобы использовать на этого бота нужно быть подписаным на канал", show_alert=True)
        await bot.send_message(callback_query.message.chat.id, "Подпишись на канал, чтобы использовать бота", reply_markup=subscribe())
        return False

