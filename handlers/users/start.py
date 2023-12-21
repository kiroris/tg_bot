from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router

#from utils.base_utils.message_check_subscription import message_check_subscription
from utils.base_utils.subscription_check import check_subscription

from keyboards.menu import menu
#from keyboards.inline import subscribe, main_menu, information, back_to_information, delete

from database.users.start.check_user_in_db import check_user_in_db
from database.users.start.add_user_to_db import add_user_to_db

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    if await check_subscription(message):
        
        user_id = message.from_user.id
        print(user_id)

        if await check_user_in_db(user_id):
            await message.answer("Привет! Ты подписан на канал и ты уже есть в БД. Это твой бот.", reply_markup=menu())
        else:
            await add_user_to_db(user_id)
            await message.answer("asd")
