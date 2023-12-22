from utils.base_utils.subscription_check import check_subscription
from database.users.start.check_user_in_db import check_user_in_db
from database.users.start.add_user_to_db import add_user_to_db
from utils.base_utils.get_user_id import get_user_id
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.menu import menu
from aiogram import Router

from database.users.payment.replenishment import replenishment_balance
from database.users.payment.debiting import debiting_balance

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    if await check_subscription(message):
        
        user_id = message.from_user.id

        #await replenishment_balance(user_id,100)
        #await debiting_balance(user_id, 100)

        if await check_user_in_db(user_id):
            await message.answer("Привет! Ты подписан на канал и ты уже есть в БД. Это твой бот.", reply_markup=menu())
        else:
            await add_user_to_db(user_id)
            await message.answer("asd", reply_markup=menu())
