import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

API_KEY = os.getenv("API_KEY")


BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city_id):
    params = {"id": city_id, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    result = response.json()

    return {
        "city_id": city_id,
        "temp": result["main"]["temp"],
        "humidity": result["main"]["humidity"],
    }
