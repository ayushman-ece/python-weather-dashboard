
from requests.exceptions import RequestException
from weather_service import get_weather


def main():
    print("=== Python Weather Dashboard ===")

    city = input("Enter city name: ").strip()

    if not city:
        print("Error: City name cannot be empty.")
        return

    try:
        weather = get_weather(city)

        print(f"\n--- Weather in {weather['city']}, {weather['country']} ---")
        print(f"Temperature : {weather['temperature']} °C")
        print(f"Feels like  : {weather['feels_like']} °C")
        print(f"Condition   : {weather['condition']}")
        print(f"Humidity    : {weather['humidity']}%")
        print(f"Wind speed  : {weather['wind_speed']} m/s")

    except ValueError as error:
        print(f"Error: {error}")

    except RequestException as error:
        print(f"Network or API error: {error}")


if __name__ == "__main__":
    main()
