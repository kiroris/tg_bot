from utils.base_utils.subscription_check import check_subscription
from aiogram.types import Message, URLInputFile
from aiogram import F, Router
from config import Config

from keyboards.kb_main_menu.main_menu import main_menu

router = Router()

@router.message(F.text == '✉️ Меню')
async def main_menu_handler(message: Message):
    if await check_subscription(message):
        image_from_url = URLInputFile("https://i.pinimg.com/564x/27/88/4f/27884f9a12aeffbd3d394a2097f5ad4d.jpg")
        await message.answer_photo(image_from_url ,caption=Config.text_main_menu, reply_markup=main_menu())