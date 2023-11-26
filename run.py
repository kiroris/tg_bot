from aiogram import Bot, Dispatcher
from config import Config
import asyncio

bot = Bot(token=Config.token)
dp = Dispatcher()

async def main():
    from handlers.users import start, main_menu
    from handlers.users.main_menu_dir import info, back_to_main_menu, support, rules


    dp.include_routers(start.router) 
    dp.include_routers(main_menu.router)

    dp.include_routers(info.router)
    dp.include_routers(back_to_main_menu.router)
    dp.include_routers(support.router)
    #dp.include_routers(back_to_information.router)
    dp.include_routers(rules.router)
    #dp.include_routers(delete_of_rules.router)







    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


    # delete cache
    import shutil
    shutil.rmtree("__pycache__")
    shutil.rmtree("handlers/__pycache__")
    shutil.rmtree("handlers/users/__pycache__")
    shutil.rmtree("handlers/users/main_menu_dir/__pycache__")

    shutil.rmtree("keyboards/__pycache__")

    shutil.rmtree("utils/__pycache__")
    shutil.rmtree("utils/base_utils/__pycache__")



    #shutil.rmtree("middlewares/__pycache__")
    #shutil.rmtree("services/__pycache__")
    #shutil.rmtree("states/__pycache__")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt , SystemExit):
        print('Bot stopped!')
