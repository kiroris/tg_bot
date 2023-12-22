from dotenv import dotenv_values
import aiopg

async def increase_balance(user_id, amount):
    config = dotenv_values()

    try:
        async with aiopg.connect(
                host=config['HOST'],
                user=config['USER'],
                password=config['PASSWORD'],
                database=config['DB_NAME']
        ) as connection:

            async with connection.cursor() as cursor:


                await cursor.execute("UPDATE users SET balance = balance + %s WHERE user_id = %s", (amount, user_id))

                return True




                #else:
                #    print(f"[INFO] User with ID {user_id} not found.")
                #    return None

    except Exception as ex:
        print("[INFO] Error when working with PostgreSQL:", ex)
        return None



