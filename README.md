# 🌦️ Python Weather Dashboard

A Python command-line application that fetches current weather information for a selected city using the OpenWeather API. It displays temperature, feels-like temperature, weather conditions, humidity, and wind speed in a readable format.

## 📌 Project Overview

The Python Weather Dashboard demonstrates how to connect a Python application to a real-world web API, process JSON data, and handle common errors.

The application accepts a city name, requests its current weather, and displays the returned information in the terminal.

**Note:** A valid, activated OpenWeather API key and an internet connection are required for live weather data.

## ✨ Features

- Fetch current weather information for a city
- Display temperature in Celsius
- Display feels-like temperature
- Show weather conditions and country code
- Display humidity and wind speed
- Process API responses using JSON
- Handle invalid city names
- Handle missing API keys and network/API errors
- Keep API credentials outside the Python source code

## 🛠️ Technologies Used

- Python
- Requests
- OpenWeather API
- JSON
- Environment variables
- Exception handling

## 📂 Project Structure

```text
python-weather-dashboard/
├── main.py
├── weather_service.py
├── requirements.txt
├── .gitignore
└── README.md
```

### File Description

| File | Purpose |
|---|---|
| `main.py` | Collects user input and displays weather information |
| `weather_service.py` | Sends the API request and processes the response |
| `requirements.txt` | Lists the required Python package |
| `.gitignore` | Excludes sensitive and unnecessary files |
| `README.md` | Documents the project |

## ⚙️ How It Works

1. The user enters a city name.
2. The application checks that the input is not empty.
3. The weather service reads the API key from an environment variable.
4. Python sends an HTTP GET request to the OpenWeather API.
5. The API returns a JSON response containing weather information.
6. The program extracts the required fields and displays them.
7. Exceptions are handled when the key is missing, a city is invalid, or a request fails.

## 🌐 API Used

**OpenWeather Current Weather API**

The application uses the current weather endpoint:

`https://api.openweathermap.org/data/2.5/weather`

The request supplies the city name, API key, and `units=metric` parameter to receive temperature values in Celsius.

API documentation: https://openweathermap.org/current

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/ayushman-ece/python-weather-dashboard.git
```

### 2. Open the project directory

```bash
cd python-weather-dashboard
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Obtain an API key

Create an account at https://openweathermap.org/api and obtain an API key. Newly created keys may take time to activate.

### 5. Set the API key

In PowerShell, run:

```powershell
$env:OPENWEATHER_API_KEY="YOUR_API_KEY_HERE"
```

Replace the placeholder with your own API key. This sets the variable for the current PowerShell session.

Do not commit your API key to GitHub.

### 6. Run the application

```bash
python main.py
```

Enter a city name when prompted.

## 📊 Example Output

The following is an illustrative example. Actual values depend on the API response and current weather.

```text
=== Python Weather Dashboard ===
Enter city name: Indore

--- Weather in Indore, IN ---
Temperature : 29.5 °C
Feels like  : 31.0 °C
Condition   : Scattered Clouds
Humidity    : 65%
Wind speed  : 3.2 m/s
```

## 📚 Concepts Learned

- HTTP requests and web APIs
- JSON data processing
- Python dictionaries
- Environment variables
- Functions and modular programming
- Exception handling
- Input validation
- API parameters and status codes
- Separating application logic from user interaction

## 🔐 Security Notes

- Never upload API keys or passwords to a public repository.
- Do not commit `.env` files.
- The `.gitignore` file helps exclude sensitive files but does not remove secrets already committed.
- If an API key is accidentally exposed, revoke or regenerate it.
- API availability and usage limits depend on the provider and account.

## ⚠️ Limitations

- Live data requires internet access and a working API key.
- Newly created API keys may take time to activate.
- The application currently supports one city per run.
- The command-line interface displays only a small selection of weather fields.
- API errors and provider limits can prevent data retrieval.

## 🔮 Future Improvements

- Add a multi-city weather comparison feature.
- Display sunrise and sunset times.
- Add weather forecasts.
- Cache recent results to reduce repeated requests.
- Build a graphical dashboard using Streamlit.
- Add automated tests with mocked API responses.

## 👨‍💻 Author

**Ayushman Tiwari**

GitHub: [ayushman-ece](https://github.com/ayushman-ece)

---

*Built as a hands-on Python project for API integration, JSON processing, and error handling.*