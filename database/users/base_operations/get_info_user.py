import aiopg
from dotenv import dotenv_values

async def get_info_user(user_id):
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
                # Получение профиля добавленного пользователя
                await cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
                result = await cursor.fetchone()

                # Проверка, найден ли пользователь с заданным ID.
                if result:
                    user_profile = {
                        'user_id': result[0],
                        'balance': result[1],
                        'seller': result[2],
                        'admin': result[3]
                    }
                    return user_profile
                else:
                    print(f"Не удалось получить профиль пользователя с ID {user_id}")
                    return None

    except Exception as ex:
        print("Ошибка при работе с PostgreSQL", ex)
        return None
