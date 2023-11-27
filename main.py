import requests
import datetime
from pprint import pprint
from config import Config
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.filters import CommandObject
from run import bot





async def get_weather(api_key, city):
    code_to_smile = {
            "Clear" : "Ясно \U00002600",
            "Clouds": "Облачно \U00002601",
            "Rain"  : "Дождь \U00002614",
            "Drizzle":"Дождь \U00002614",
            "Thunderstorm": "Гроза \U000026A1",
            "Snow"  : "Снег \U0001F328",
            "Mist"  : "Туман \U0001F32B",
        }

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'lang': 'ru',
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        city = data["name"]
        temperature = data["main"]["temp"]
        weather_description = data['weather'][0]['main']
        description = data['weather'][0]['description'].capitalize()
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = data['weather'][0]['description'].capitalize()
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
            
        return(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:')}***\n"
              f"Погода в городе: {city}\nТемпература: {temperature}C° {wd}\nПодробности о погоде: {description}\n"
              f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/c\n"
              f"Восход слонца: {sunrise_timestamp} AM\nЗакат солнца: {sunset_timestamp} PM\nПродолжительность дня: {length_of_day}")

    except Exception as e:
        return f'\n00002620 Не удалось получить погоду для {city}.Проверьте название города. Статус код: {response.status_code}, текст ошибки: {response.content.decode("utf-8")} \n00002620'
        print(e)
        

router = Router()


@router.message(Command("weather"))
async def send_weather(message: Message, command: CommandObject):
    if command.args:
        await bot.send_message(message,chat.id,result = get_weather(Config.OpenWeatherToken, command.args))
        result = get_weather(Config.OpenWeatherToken, command.args)
        print(result)
    else:
        await message.answer("Пожалуйста, укажите что-то после команды")









result = get_weather(Config.OpenWeatherToken, city_name)
print(result)

