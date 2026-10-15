
import os
import requests


API_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        raise ValueError(
            "API key not found. Set OPENWEATHER_API_KEY first."
        )

    response = requests.get(
        API_URL,
        params={
            "q": city,
            "appid": api_key,
            "units": "metric",
        },
        timeout=10,
    )

    if response.status_code == 404:
        raise ValueError("City not found. Check the spelling.")

    response.raise_for_status()
    data = response.json()

    return {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "condition": data["weather"][0]["description"].title(),
        "wind_speed": data["wind"]["speed"],
    }
