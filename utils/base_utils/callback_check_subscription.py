from aiogram.types import CallbackQuery
from config import Config
from run import bot

from keyboards.base_kb.subscribe import subscribe

#==========CHECK_SUBSCRIPTION(FOR_CALLBACK)==========#
async def callback_check_subscription(callback_query: CallbackQuery):
        chat_member = await bot.get_chat_member(Config.id_channel, callback_query.from_user.id)

        if chat_member.status == "member":
            return True
        elif chat_member.status == "administrator" or chat_member.status == "creator":
            return True
        else:
            await bot.answer_callback_query(callback_query.id, "Чтобы использовать на этого бота нужно быть подписаным на канал", show_alert=True)
            await bot.send_message(callback_query.message.chat.id, "Привет, подпишись на канал, чтобы использовать этого бота", reply_markup=subscribe())
            return False
