from aiogram import Bot, Dispatcher
from dotenv import dotenv_values
import asyncio

config = dotenv_values()
bot = Bot(config['TOKEN_BOT'])
dp = Dispatcher()

async def main():
    from handlers.users import start
    


    dp.include_routers(start.router) 
    

    # Main Menu
    from handlers.users.main_menu_dir import main_menu
    dp.include_routers(main_menu.router)

    # Support Section
    from handlers.users.main_menu_dir.support_section import info, support, rules
    dp.include_routers(info.router)

    dp.include_routers(support.router)
    dp.include_routers(rules.router)

    from handlers.users.main_menu_dir.base_handlers import back_to_main_menu
    dp.include_routers(back_to_main_menu.router)

    # Profile
    from handlers.users.main_menu_dir.profile import profile
    dp.include_routers(profile.router)










    #from modules import check_weather
    #dp.include_routers(check_weather.router)
    
    #from modules import check_price_crypto
    #dp.include_routers(check_price_crypto.router)





    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()






    # DELETE OF CACHE
    import shutil
    cleanup_directories = [
        "__pycache__",
        # handlers
        "handlers/__pycache__",
        "handlers/users/__pycache__",
        "handlers/users/main_menu_dir/__pycache__",
        "handlers/users/main_menu_dir/profile/__pycache__",
        "handlers/users/main_menu_dir/base_handlers/__pycache__",
        "handlers/users/main_menu_dir/support_section/__pycache__",

        # keyboards
        "keyboards/__pycache__",
        "keyboards/base_kb/__pycache__",
        "keyboards/kb_main_menu/__pycache__",
        "keyboards/kb_main_menu/profile/__pycache__",
        "keyboards/kb_main_menu/support_section/__pycache__",

        # utils
        "utils/__pycache__",
        "utils/base_utils/__pycache__",

        # modules
        "modules/__pycache__",
        "modules/base_modules/__pycache__",

        # database
        "database/__pycache__",
        "database/users/__pycache__",
        "database/users/start/__pycache__",
        "database/users/payment/__pycache__",
        "database/users/base_operations/__pycache__",
    ]

    for directory in cleanup_directories:
        try:
            shutil.rmtree(directory)
        except FileNotFoundError:
            pass

    
    
    #shutil.rmtree("__pycache__")


    ## HANDLESRS
    #shutil.rmtree("handlers/__pycache__")
    ## users
    #shutil.rmtree("handlers/users/__pycache__")
    ## main_menu_dir
    #shutil.rmtree("handlers/users/main_menu_dir/__pycache__")
    ## personal_account
    #shutil.rmtree("handlers/users/main_menu_dir/personal_account/__pycache__")
    ## support_section
    #shutil.rmtree("handlers/users/main_menu_dir/support_section/__pycache__")



    ## KEYBOARDS
    ##shutil.rmtree("/keyboards/__pycache__")
    #shutil.rmtree("/keyboards/base_kb/__pycache__")
    #shutil.rmtree("/keyboards/kb_main_menu/__pycache__")
    ##shutil.rmtree("/keyboards/kb_main_menu/personal_account/__pycache__")
    ##shutil.rmtree("/keyboards/kb_main_menu/support_section/__pycache__")


    #

    ## UTILS
    #shutil.rmtree("utils/__pycache__")
    ## base utils
    #shutil.rmtree("utils/base_utils/__pycache__")


    ## MODULES
    ##shutil.rmtree("modules/__pycache__")
    ## base modules
    ##shutil.rmtree("modules/base_modules/__pycache__")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt , SystemExit):
        print('Bot stopped!')
