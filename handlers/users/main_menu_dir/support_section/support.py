from keyboards.kb_main_menu.support_section.back_to_information import back_to_information
from utils.base_utils.subscription_check import check_subscription
from utils.base_utils.error_handler import error_handler
from aiogram.types import CallbackQuery
from aiogram import F, Router
from config import Config
from run import bot

router = Router()

#==========SUPPORT==========#
@router.callback_query(F.data == 'support')
async def process_callback_support(callback_query: CallbackQuery):
    if await check_subscription(callback_query):
        try:
            await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                           message_id=callback_query.message.message_id,
                                           caption=Config.support_text,
                                           reply_markup=back_to_information())
        except Exception as e:
            await error_handler(callback_query, e)
