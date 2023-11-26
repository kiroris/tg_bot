from utils.base_utils.callback_check_subscription import callback_check_subscription
from utils.base_utils.error_handler import error_handler
from aiogram.types import CallbackQuery
from aiogram import F, Router
from config import Config
from run import bot

from keyboards.inline import main_menu

router = Router()

#==========BACK_TO_MAIN_MENU==========#
@router.callback_query(F.data == 'back_to_main_menu')
async def process_callback_back_to_main_menu(callback_query: CallbackQuery):
    if await callback_check_subscription(callback_query):
        try:
            await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                           message_id=callback_query.message.message_id,
                                           caption=Config.text_main_menu,
                                           reply_markup=main_menu())
        except Exception as e:
            await error_handler(callback_query, e)

