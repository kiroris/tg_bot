from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router

#from utils.base_utils.message_check_subscription import message_check_subscription
from utils.base_utils.subscription_check import check_subscription

from keyboards.menu import menu
#from keyboards.inline import subscribe, main_menu, information, back_to_information, delete



router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    if await check_subscription(message):
        await message.answer("Привет! Ты подписан на канал. Это твой бот.", reply_markup=menu())
