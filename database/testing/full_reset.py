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

            # Полная очистка таблицы перед вставкой новых данных
            await cursor.execute('DELETE FROM countries')

            # Вставка данных о странах в таблицу Countries
            for country_id, country_info in countries.items():
                try:
                    country_id = int(country_id)
                    country_eng = country_info['eng']
                    country_rus = country_info['rus']
                    await cursor.execute('''
                        INSERT INTO countries (country_id, country_eng, country_rus) VALUES (%s, %s, %s)
                        ''', (country_id, country_eng, country_rus))
                except KeyError as e:
                    print(f"KeyError: {e}")
