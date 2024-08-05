import aiohttp
import asyncio
from datetime import datetime
import os
from .models import WeatherData
from . import db

OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')
OPENWEATHER_URL = 'https://api.openweathermap.org/data/2.5/group'


async def fetch_weather(session, city_id):
    params = {
        'id': city_id,
        'units': 'metric',
        'appid': OPENWEATHER_API_KEY
    }
    async with session.get(OPENWEATHER_URL, params=params) as response:
        return await response.json()


async def collect_weather_data(user_defined_id, city_ids):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_weather(session, city_id) for city_id in city_ids]
        weather_data = await asyncio.gather(*tasks)

    data = {
        'city_ids': city_ids,
        'weather': weather_data
    }

    new_entry = WeatherData(
        user_defined_id=user_defined_id,
        data=data
    )
    db.session.add(new_entry)
    db.session.commit()


def get_weather_data(user_defined_id):
    entry = WeatherData.query.filter_by(user_defined_id=user_defined_id).first()
    if entry:
        return entry.data
    return None
