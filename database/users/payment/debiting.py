from dotenv import dotenv_values
import asyncio
import aiopg

async def debiting_balance(user_id, amount):
    config = dotenv_values()

    try:
        async with aiopg.connect(
                host=config['HOST'],
                user=config['USER'],
                password=config['PASSWORD'],
                database=config['DB_NAME']
        ) as connection:

            async with connection.cursor() as cursor:
                await cursor.execute("UPDATE users SET balance = balance - %s WHERE user_id = %s", (amount, user_id))
                return True

    except Exception as ex:
        print("[INFO] Error when working with PostgreSQL:", ex)
        return False
