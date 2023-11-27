import requests
import datetime
from config import Config
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.filters import CommandObject
from run import bot

async def get_weather(api_key, city, message):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B",
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
        length_of_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        await message.answer(
            f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:')}***\n"
            f"Погода в городе: {city}\nТемпература: {temperature}C° {wd}\nПодробности о погоде: {description}\n"
            f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/c\n"
            f"Восход слонца: {sunrise_timestamp} AM\nЗакат солнца: {sunset_timestamp} PM\nПродолжительность дня: {length_of_day}")

    except Exception as e:
        await message.answer(
                f'Не удалось получить погоду для города: {city}.\nПроверьте пожалуйста название города\nСтатус код: {response.status_code} \U00002620 \U00002620 \U00002620')
        print(e)

router = Router()

@router.message(Command("weather"))
async def send_weather_data(message: Message, command: CommandObject):
    if command.args:
        await get_weather(Config.OpenWeatherToken, command.args, message)  # Передаем объект сообщения в функцию
    else:
        await message.answer("Пожалуйста укажите навазние города после команды 'weather'\nПример: /weather Москва ")

