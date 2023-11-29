from utils.base_utils.callback_check_subscription import callback_check_subscription
from utils.base_utils.error_handler import error_handler
from aiogram.types import CallbackQuery
from aiogram import Router, F
from config import Config
from run import bot

from keyboards.inline import information

router = Router()

#==========INFO==========#
@router.callback_query(F.data == 'info')
async def process_callback_information(callback_query: CallbackQuery):
    if await callback_check_subscription(callback_query):
        try:
            await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                           message_id=callback_query.message.message_id,
                                           caption=Config.information_text,
                                           reply_markup=information())
        except Exception as e:
            await error_handler(callback_query, e)



#==========INFO==========#
@router.callback_query(F.data == 'back_to_information')
async def process_callback_back_to_information(callback_query: CallbackQuery):
    if await callback_check_subscription(callback_query):
        try:
            await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                           message_id=callback_query.message.message_id,
                                           caption=Config.information_text,
                                           reply_markup=information())
        except Exception as e:
            await error_handler(callback_query, e)