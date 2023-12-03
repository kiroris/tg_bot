from aiogram import Router, F
from utils.base_utils.callback_check_subscription import callback_check_subscription
from utils.base_utils.error_handler import error_handler
from aiogram.types import CallbackQuery
from run import bot

from keyboards.kb_main_menu.personal_account.profile_menu import profile_menu



router = Router()


@router.callback_query(F.data == 'personal_account')
async def process_callback_personal_account(callback_query: CallbackQuery):
    if await callback_check_subscription(callback_query):
        try:
            account = f"""
            Баланс: None
            ID пользователя: {callback_query.from_user.id}
            """

            await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                           message_id=callback_query.message.message_id,
                                           caption=account,
                                           reply_markup=profile_menu())
        except Exception as e:
            await error_handler(callback_query, e)
