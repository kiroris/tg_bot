from database.users.base_operations.get_info_user import get_info_user
from keyboards.kb_main_menu.profile.profile_menu import profile_menu
from utils.base_utils.subscription_check import check_subscription
from utils.base_utils.error_handler import error_handler
from aiogram.types import CallbackQuery
from aiogram import Router, F
from config import Config
from run import bot

router = Router()

@router.callback_query(F.data == 'profile')
async def process_callback_profile(callback_query: CallbackQuery):
    if await check_subscription(callback_query):
        try:
            user_id = callback_query.from_user.id
            profile = await get_info_user(user_id)

            await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                           message_id=callback_query.message.message_id,
                                           caption=profile,#Config.text_profile,
                                           parse_mode="Markdown",
                                           reply_markup=profile_menu())
        except Exception as e:
            await error_handler(callback_query, e)
