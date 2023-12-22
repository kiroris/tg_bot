from dotenv import dotenv_values
import aiopg

async def get_info_user(user_id):
    config = dotenv_values()

    try:
        async with aiopg.connect(
                host=config['HOST'],
                user=config['USER'],
                password=config['PASSWORD'],
                database=config['DB_NAME']
        ) as connection:

            async with connection.cursor() as cursor:
                await cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
                result = await cursor.fetchone()

                if result:
                    user_profile = {
                        'user_id': result[0],
                        'balance': result[1],
                        'seller': result[2],
                        'admin': result[3]
                    }

                    admin_status = "Админ ✅" if user_profile['admin'] else "Админ ❌"
                    profile_text = f"""
*Ваш ID:* `{user_profile['user_id']}`
*Баланс:* __{user_profile['balance']}__
*{admin_status}*
"""
                    return profile_text

                else:
                    print(f"Не удалось получить профиль пользователя с ID {user_id}")
                    return None

    except Exception as ex:
        print("Ошибка при работе с PostgreSQL", ex)
        return None

