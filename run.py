from aiogram import Bot, Dispatcher
from config import Config
import asyncio

bot = Bot(token=Config.token)
dp = Dispatcher()

async def main():
#    from handlers import command_start
    #dp.include_router(command_start.router)

    from handlers.user import dp

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()




    # delete cache
    import shutil
    shutil.rmtree("__pycache__")
    shutil.rmtree("handlers/__pycache__")
    shutil.rmtree("keyboards/__pycache__")
    #shutil.rmtree("middlewares/__pycache__")
    #shutil.rmtree("services/__pycache__")
    #shutil.rmtree("states/__pycache__")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt , SystemExit):
        print('Bot stopped!')
