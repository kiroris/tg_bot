from aiogram.filters import Command
from aiogram.types import Message, URLInputFile
from config import Config
from aiogram import F
from aiogram import types
from run import bot, dp

from aiogram.types import CallbackQuery


from keyboards.default import menu
from keyboards.inline import subscribe, main_menu, information, back_to_information, delete




#==========CHECK_SUBSCRIPTION(FOR_MESSAGE/COMMAND)==========#
async def check_subscription(message: Message):
        chat_member = await bot.get_chat_member(Config.id_channel, message.from_user.id)

        if chat_member.status == "member":
            return True
        elif chat_member.status == "administrator" or chat_member.status == "creator":
            return True
        else:
            await bot.send_message(message.chat.id, "Привет, подпишись на канал, чтобы использовать бота", reply_markup=subscribe())
            return False


#==========CHECK_SUBSCRIPTION(FOR_CALLBACK)==========#
async def check_subscription_callback(callback_query: CallbackQuery):
        chat_member = await bot.get_chat_member(Config.id_channel, callback_query.from_user.id)

        if chat_member.status == "member":
            return True
        elif chat_member.status == "administrator" or chat_member.status == "creator":
            return True
        else:
            await bot.answer_callback_query(callback_query.id, "Чтобы использовать на этого бота нужно быть подписаным на канал", show_alert=True)
            await bot.send_message(callback_query.message.chat.id, "Привет, подпишись на канал, чтобы использовать этого бота", reply_markup=subscribe())
            return False




#==========START==========#
@dp.message(Command("start"))
async def cmd_start(message: Message):
    if await check_subscription(message):
        await message.answer("Привет! Ты подписан на канал. Это твой бот.", reply_markup=menu())



#==========MENU==========#
@dp.message(F.text == '✉️ Меню')
async def main_menu_handler(message: Message):
    if await check_subscription(message):
        image_from_url = URLInputFile("https://i.pinimg.com/564x/27/88/4f/27884f9a12aeffbd3d394a2097f5ad4d.jpg")
        await message.answer_photo(image_from_url ,caption=Config.text_main_menu, reply_markup=main_menu())

# Go to main menu
@dp.callback_query(F.data == 'go_to_main_menu')
async def process_callback_last_button(callback_query: CallbackQuery):
    if await check_subscription_callback(callback_query):
        try:
            await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                           message_id=callback_query.message.message_id,
                                           caption=Config.text_main_menu,
                                           reply_markup=main_menu())
        except Exception as e:
            print(f"An error occurred: {e}")
            await bot.answer_callback_query(callback_query.id, text="Пожалуйста, повторите попытку позже...")



#==========INFO==========#
@dp.callback_query(F.data == 'info')
async def callback_info(callback_query: CallbackQuery):
    if await check_subscription_callback(callback_query):
        try:
            await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                           message_id=callback_query.message.message_id,
                                           caption=Config.information_text,
                                           reply_markup=information())
        except Exception as e:
            print(f"An error occurred: {e}")
            await bot.answer_callback_query(callback_query.id, text="Пожалуйста, повторите попытку позже...")

# Back to information
@dp.callback_query(F.data == 'back_to_information')
async def callback_info(callback_query: CallbackQuery):
    if await check_subscription_callback(callback_query):
        try:
            await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                           message_id=callback_query.message.message_id,
                                           caption=Config.information_text,
                                           reply_markup=information())
        except Exception as e:
            print(f"An error occurred: {e}")
            await bot.answer_callback_query(callback_query.id, text="Пожалуйста, повторите попытку позже...")



#==========SUPPORT==========#
@dp.callback_query(F.data == 'support')
async def callback_info(callback_query: CallbackQuery):
    if await check_subscription_callback(callback_query):
        try:
            await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                           message_id=callback_query.message.message_id,
                                           caption=Config.support_text,
                                           reply_markup=back_to_information())
        except Exception as e:
            print(f"An error occurred: {e}")
            await bot.answer_callback_query(callback_query.id, text="Пожалуйста, повторите попытку позже...")



#==========RULES==========#
@dp.callback_query(F.data == 'rules')
async def callback_info(callback_query: CallbackQuery):
    if await check_subscription_callback(callback_query):
        try:
            await bot.send_message(callback_query.message.chat.id,Config.rules, reply_markup=delete())
        except Exception as e:
            print(f"An error occurred: {e}")
            await bot.answer_callback_query(callback_query.id, text="Пожалуйста, повторите попытку позже...")

# Delete of rules
@dp.callback_query(F.data == 'delete')
async def callback_info(callback_query: CallbackQuery):
    if await check_subscription_callback(callback_query):
        try:
            await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
        except Exception as e:
            print(f"An error occurred: {e}")
            await bot.answer_callback_query(callback_query.id, text="Пожалуйста, повторите попытку позже...")









