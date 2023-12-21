from aiogram import Router, F
from utils.base_utils.subscription_check import check_subscription
from utils.base_utils.error_handler import error_handler
from aiogram.types import CallbackQuery
from run import bot
from config import Config

from keyboards.kb_main_menu.profile.profile_menu import profile_menu

from database.get_profile_users import get_profile_users

router = Router()


@router.callback_query(F.data == 'profile')
async def process_callback_profile(callback_query: CallbackQuery):
    if await check_subscription(callback_query):
        try:
            user_id = callback_query.from_user.id
            profile_data = await get_profile_users(user_id)
            
            if profile_data:
                user_id = profile_data['user_id']
                balance = profile_data['balance']
                is_seller = profile_data['seller']
                is_admin = profile_data['admin']

                seller_status = "Продавец ✅" if is_seller else "Продавец ❌"
                admin_status = "Админ ✅" if is_admin else "Админ ❌"

                profile = f"""
*Ваш ID:* `{user_id}`
*Баланс:* __{balance}__
*{admin_status}*
"""
            await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                           message_id=callback_query.message.message_id,
                                           caption=profile,#Config.text_profile,
                                           parse_mode="Markdown",
                                           reply_markup=profile_menu())
        except Exception as e:
            await error_handler(callback_query, e)
