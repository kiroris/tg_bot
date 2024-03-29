from utils.base_utils.subscription_check import check_subscription
from database.users.start.check_user_in_db import check_user_in_db
from database.users.start.add_user_to_db import add_user_to_db
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

        if await check_user_in_db(user_id):
            await message.answer("Привет, ты не впервые.", reply_markup=menu())
        else:
            await add_user_to_db(user_id)
            await message.answer("Привет, ты впервые", reply_markup=menu())
