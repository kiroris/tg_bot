import asyncio
from dotenv import dotenv_values
import aiopg
from smsactivate.api import SMSActivateAPI

async def check_country_match():
    config = dotenv_values()

    # Подключение к базе данных
    async with aiopg.connect(
            host=config['HOST'],
            user=config['USER'],
            password=config['PASSWORD'],
            database=config['DB_NAME']
    ) as connection:

        async with connection.cursor() as cursor:
            # Получение списка стран из SMSActivate API
            API_KEY = '6675e29de251cc3e5e5747d46A472e25'
            sa = SMSActivateAPI(API_KEY)
            api_countries = sa.getCountries()

            # Получение списка стран из базы данных
            await cursor.execute('SELECT country_id, country_eng FROM countries')
            db_countries = {row[0]: row[1] for row in await cursor.fetchall()}

            # Проверка совпадения стран
            for api_country_id, api_country_name in api_countries.items():
                try:
                    api_country_id = int(api_country_id)
                    api_country_name_eng = api_country_name.get('eng', None)
                    
                    if api_country_name_eng:
                        db_country_name = db_countries.get(api_country_id, None)

                        # Проверка совпадения названий стран
                        if db_country_name and db_country_name == api_country_name_eng:
                            continue
                        else:
                            return False

                except ValueError as e:
                    print(f"ValueError: {e}")
                    return False
                except Exception as e:
                    print(f"Error checking country match: {e}")
                    return False

            # Если все страны совпали
            return True
