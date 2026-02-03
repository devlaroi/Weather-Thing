---

A **Python CLI application** that automatically detects your location and displays **current weather**, **5-day forecast**, and **air quality**, using the free **OpenWeatherMap** API.

The project’s goal is to provide detailed meteorological information directly in the terminal, in a simple and informative way.

---

## ✨ Features

* 📍 **Automatic location detection** via IP (with manual fallback)
* 🌡️ **Current weather**

  * Current, minimum, and maximum temperature
  * Feels-like temperature
  * Humidity, pressure, and visibility
  * Cloud coverage
* 🌬️ **Wind data**

  * Speed
  * Direction (cardinal)
  * Gusts (when available)
* 🔥❄️ **Advanced calculations**

  * Heat Index
  * Wind Chill
* 🌅 **Local times**

  * Sunrise and sunset adjusted to the local timezone
* 🌫️ **Air Quality (AQI)**

  * Classification (Good → Very Poor)
  * Health recommendations
* 📆 **5-day forecast**

  * 3-hour intervals
  * Temperature and feels-like
  * Precipitation probability
  * Rain, snow, and wind

---

## 🧰 Technologies Used

* Python 3
* [`requests`](https://docs.python-requests.org/)
* [`pytz`](https://pypi.org/project/pytz/)
* [OpenWeatherMap API](https://openweathermap.org/api)
* IP-based geolocation service (`ipinfo.io`)

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/pabloarzaoo/Weather-Thing
```

2. Install the dependencies:

```bash
pip install requests pytz
```

---

## 🔑 API Configuration

This project uses the **free OpenWeatherMap API**.

1. Create an account at:
   [https://openweathermap.org/api](https://openweathermap.org/api)
2. Generate your **API Key**
3. Replace the key in the code:

```python
api_key = 'YOUR_API_KEY_HERE'
```

⚠️ **Important:** It is not recommended to commit your API key to public repositories.

---

## ▶️ How to Use

Run the script:

```bash
python weather.py
```

The program will:

1. Validate the API key
2. Automatically detect your location
3. Fetch current weather data
4. Display a detailed 5-day forecast
5. Show air quality information (when available)

---

## 🧠 Notes

* If automatic detection fails, the program will ask for manual input
* The free API may have availability limitations for air quality data in some regions
* All times are adjusted to the **detected local timezone**

---

## 📄 License

This project is distributed under the **MIT** license.
Feel free to use, modify, and distribute it.

---

## 🚀 Future Ideas

* Export data to JSON or CSV
* Local cache to reduce API calls
* Multi-language support
* Weather alerts

---
