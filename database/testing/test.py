import asyncio
from dotenv import dotenv_values
import aiopg
from smsactivate.api import SMSActivateAPI

async def update():
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
            countries = sa.getCountries()

            # Вставка данных о странах в таблицу Countries
            for country_id, country_info in countries.items():
                try:
                    api_country_id = int(country_id)
                    country_name = country_info['eng']
                    await cursor.execute('''
                        INSERT INTO Countries (api_country_id, country_name) VALUES (%s, %s)
                        ON CONFLICT (api_country_id) DO NOTHING
                    ''', (api_country_id, country_name))
                except KeyError as e:
                    print(f"KeyError: {e}")
