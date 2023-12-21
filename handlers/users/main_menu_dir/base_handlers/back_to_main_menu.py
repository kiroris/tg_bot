from utils.base_utils.subscription_check import check_subscription
from utils.base_utils.error_handler import error_handler
from aiogram.types import CallbackQuery
from aiogram import F, Router
from config import Config
from run import bot

from keyboards.kb_main_menu.main_menu import main_menu
from database.base_operations.get_info_user import get_info_user

router = Router()

#==========BACK_TO_MAIN_MENU==========#
@router.callback_query(F.data == 'back_to_main_menu')
async def process_callback_back_to_main_menu(callback_query: CallbackQuery):
    if await check_subscription(callback_query):
        try:
            
            user_id = message.from_user.id
            profile_data = await get_profile_users(user_id)

            if profile_data:
                user_id = profile_data['user_id']
                balance = profile_data['balance']
                is_seller = profile_data['seller']
                is_admin = profile_data['admin']

                seller_status = "Продавец ✅" if is_seller else "Продавец ❌"
                #admin_status = "Админ ✅" if is_admin else "Админ ❌"

                profile = f"""
*Ваш ID:* `{user_id}`
*Баланс:* __{balance}__
*{admin_status}*
"""


            await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                           message_id=callback_query.message.message_id,
                                           caption=profile,
                                           parse_mode='Markdown',
                                           reply_markup=main_menu())
        except Exception as e:
            await error_handler(callback_query, e)

