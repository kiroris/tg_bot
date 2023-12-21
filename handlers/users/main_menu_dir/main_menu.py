from database.users.base_operations.get_info_user import get_info_user
from utils.base_utils.subscription_check import check_subscription
from keyboards.kb_main_menu.main_menu import main_menu
from aiogram.types import Message, URLInputFile
from aiogram import F, Router
from config import Config

router = Router()

@router.message(F.text == '✉️ Меню')
async def main_menu_handler(message: Message):
    if await check_subscription(message):

        image_from_url = URLInputFile("https://i.pinimg.com/564x/27/88/4f/27884f9a12aeffbd3d394a2097f5ad4d.jpg")
        user_id = message.from_user.id
        profile_data = await get_info_user(user_id)

        if profile_data:
            user_id = profile_data['user_id']
            balance = profile_data['balance']
            is_seller = profile_data['seller']
            is_admin = profile_data['admin']

            #seller_status = "Продавец ✅" if is_seller else "Продавец ❌"
            admin_status = "Админ ✅" if is_admin else "Админ ❌"

            profile = f"""
*Ваш ID:* `{user_id}`
*Баланс:* __{balance}__
*{admin_status}*
"""

        await message.answer_photo(image_from_url,caption=profile,parse_mode="Markdown", reply_markup=main_menu())
