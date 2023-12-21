import asyncio
import aiopg
from dotenv import dotenv_values

async def get_profile_users(user_id):
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
                # Получение профиля пользователя
                await cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
                result = await cursor.fetchone()

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

async def main():
    user_id = 6933650402  # Замените на конкретный user_id
    profile_data = await get_profile_users(user_id)

    if profile_data:
        print("User Profile:")
        print(f"User ID: {profile_data['user_id']}")
        print(f"Balance: {profile_data['balance']}")
        print(f"Seller: {profile_data['seller']}")
        print(f"Admin: {profile_data['admin']}")
    else:
        print(f"User with ID {user_id} not found.")

# Запуск асинхронной программы
if __name__ == "__main__":
    asyncio.run(main())

