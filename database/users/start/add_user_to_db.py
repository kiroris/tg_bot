from dotenv import dotenv_values
import aiopg

async def add_user_to_db(user_id):
    config = dotenv_values()

    try:
        # Подключение к базе данных
        async with aiopg.connect(
                host=config['HOST'],
                user=config['USER'],
                password=config['PASSWORD'],
                database=config['DB_NAME']
        ) as connection:

            async with connection.cursor() as cursor:
                # Добавление нового пользователя
                await cursor.execute("INSERT INTO users (user_id, balance, seller, admin) VALUES (%s, %s, %s, %s)",
                                   (user_id, 0.0, False, False))
                print(f"[INFO] User with ID: {user_id} has been added to the database")

    except Exception as ex:
        print("[INFO] Error when working with PostgreSQL:", ex)
