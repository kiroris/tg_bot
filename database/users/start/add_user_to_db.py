import aiopg
from dotenv import dotenv_values

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
                print("Пользователь добавлен в базу данных")

    except Exception as ex:
        print("Ошибка при работе с PostgreSQL", ex)