from aiogram.types import CallbackQuery
from aiogram import types
from run import bot

async def error_handler(callback_query: CallbackQuery, error: Exception):
    print(f"An error occurred: {error}")
    await bot.answer_callback_query(callback_query.id, text="Пожалуйста, повторите попытку позже...")
