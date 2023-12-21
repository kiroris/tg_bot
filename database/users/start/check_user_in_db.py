from dotenv import dotenv_values
import aiopg

async def check_user_in_db(user_id):
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
                # Проверка наличия пользователя в базе данных
                await cursor.execute("SELECT EXISTS(SELECT 1 FROM users WHERE user_id = %s)", (user_id,))
                user_exists = await cursor.fetchone()
                
                return user_exists[0]  

    except Exception as ex:
        print("Ошибка при работе с PostgreSQL", ex)
        return False

