from aiogram.types import Message
from config import Config
from run import bot

from keyboards.inline import subscribe

#==========CHECK_SUBSCRIPTION(FOR_MESSAGE/COMMAND)==========#
async def message_check_subscription(message: Message):
        chat_member = await bot.get_chat_member(Config.id_channel, message.from_user.id)

        if chat_member.status == "member":
            return True
        elif chat_member.status == "administrator" or chat_member.status == "creator":
            return True
        else:
            await bot.send_message(message.chat.id, "Привет, подпишись на канал, чтобы использовать бота", reply_markup=subscribe())
            return False

