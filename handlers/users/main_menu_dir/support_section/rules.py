from utils.base_utils.subscription_check import check_subscription
from utils.base_utils.error_handler import error_handler
from keyboards.base_kb.delete import delete
from aiogram.types import CallbackQuery
from aiogram import Router, F
from config import Config
from run import bot

router = Router()

#==========RULES==========#
@router.callback_query(F.data == 'rules')
async def process_callback_rules(callback_query: CallbackQuery):
    if await check_subscription(callback_query):
        try:
            await bot.send_message(callback_query.message.chat.id,Config.rules, reply_markup=delete())
        except Exception as e:
            await error_handler(callback_query, e)

#==========DELETE_OF_RULES==========#
@router.callback_query(F.data == 'delete')
async def callback_info(callback_query: CallbackQuery):
    if await check_subscription(callback_query):
        try:
            await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
        except Exception as e:
            await error_handler(callback_query, e)
