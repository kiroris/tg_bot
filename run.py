from aiogram import Bot, Dispatcher
from config import Config
import asyncio

bot = Bot(token=Config.token)
dp = Dispatcher()

async def main():
    from handlers.users import start
    


    dp.include_routers(start.router) 
    

    # Main Menu
    from handlers.users.main_menu_dir import main_menu
    dp.include_routers(main_menu.router)

    # Support Section
    from handlers.users.main_menu_dir.support_section import info, back_to_main_menu, support, rules
    dp.include_routers(info.router)
    dp.include_routers(back_to_main_menu.router)
    dp.include_routers(support.router)
    dp.include_routers(rules.router)

    # Personal Account
    from handlers.users.main_menu_dir.personal_account import personal_account
    dp.include_routers(personal_account.router)










    #from modules import check_weather
    #dp.include_routers(check_weather.router)
    
    #from modules import check_price_crypto
    #dp.include_routers(check_price_crypto.router)





    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


    # delete cache
    import shutil
    shutil.rmtree("__pycache__")


    # HANDLESRS
    shutil.rmtree("handlers/__pycache__")
    # users
    shutil.rmtree("handlers/users/__pycache__")
    # main_menu_dir
    shutil.rmtree("handlers/users/main_menu_dir/__pycache__")
    # personal_account
    shutil.rmtree("handlers/users/main_menu_dir/personal_account/__pycache__")
    # support_section
    shutil.rmtree("handlers/users/main_menu_dir/support_section/__pycache__")



    # KEYBOARDS



    

    # UTILS
    shutil.rmtree("utils/__pycache__")
    # base utils
    shutil.rmtree("utils/base_utils/__pycache__")


    # MODULES
    #shutil.rmtree("modules/__pycache__")
    # base modules
    #shutil.rmtree("modules/base_modules/__pycache__")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt , SystemExit):
        print('Bot stopped!')
