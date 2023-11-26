from utils.base_utils.callback_check_subscription import callback_check_subscription
from utils.base_utils.error_handler import error_handler
from aiogram.types import CallbackQuery
from aiogram import F, Router
from config import Config
from run import bot


from keyboards.inline import back_to_information


router = Router()

#==========SUPPORT==========#
@router.callback_query(F.data == 'support')
async def process_callback_support(callback_query: CallbackQuery):
    if await callback_check_subscription(callback_query):
        try:
            await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                           message_id=callback_query.message.message_id,
                                           caption=Config.support_text,
                                           reply_markup=back_to_information())
        except Exception as e:
            await error_handler(callback_query, e)
