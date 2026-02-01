import requests
import json
from datetime import datetime
import pytz

def get_location():
    try:
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        city = data.get('city', 'Unknown')
        region = data.get('region', 'Unknown')
        country = data.get('country', 'Unknown')
        loc = data.get('loc', '0,0').split(',')
        lat, lon = float(loc[0]), float(loc[1])
        timezone = data.get('timezone', 'UTC')
        return city, region, country, lat, lon, timezone
    except Exception as e:
        print(f"Error getting location: {e}")
        print("Falling back to manual input...")
        city = input("Enter your city: ")
        region = input("Enter your region/state: ")
        country = input("Enter your country: ")
        lat = float(input("Enter latitude: "))
        lon = float(input("Enter longitude: "))
        timezone = input("Enter timezone (e.g., America/New_York): ")
        return city, region, country, lat, lon, timezone

def get_current_weather_data(lat, lon, api_key):
    """Get current weather data using free API"""
    try:
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=en'
        response = requests.get(url)
        data = response.json()
        if response.status_code != 200:
            print(f"API Error: {data.get('message', 'Unknown error')} (Code: {response.status_code})")
            return None
        return data
    except Exception as e:
        print(f"Error getting current weather data: {e}")
        return None

def get_forecast_data(lat, lon, api_key):
    """Get 5-day forecast using free API"""
    try:
        url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=en'
        response = requests.get(url)
        data = response.json()
        if response.status_code != 200:
            print(f"API Error: {data.get('message', 'Unknown error')} (Code: {response.status_code})")
            return None
        return data
    except Exception as e:
        print(f"Error getting forecast data: {e}")
        return None

def get_air_quality(lat, lon, api_key):
    try:
        url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}'
        response = requests.get(url)
        data = response.json()
        if 'list' in data and data['list']:
            aqi = data['list'][0]['main']['aqi']
            components = data['list'][0]['components']
            return aqi, components
        return None, None
    except Exception as e:
        print(f"Error getting air quality: {e}")
        return None, None

def wind_direction(deg):
    if deg is None:
        return 'N/A'
    directions = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    index = round(deg / 22.5) % 16
    return directions[index]

def calculate_heat_index(temp, humidity):
    if temp < 27:
        return None
    hi = -42.379 + 2.04901523 * temp + 10.14333127 * humidity - 0.22475541 * temp * humidity - 0.00683783 * temp**2 - 0.05481717 * humidity**2 + 0.00122874 * temp**2 * humidity + 0.00085282 * temp * humidity**2 - 0.00000199 * temp**2 * humidity**2
    return hi

def calculate_wind_chill(temp, wind_speed):
    if temp > 10 or wind_speed < 4.8:
        return None
    wc = 13.12 + 0.6215 * temp - 11.37 * (wind_speed ** 0.16) + 0.3965 * temp * (wind_speed ** 0.16)
    return wc

def test_api_key(api_key):
    """Test if API key is valid"""
    test_url = f'https://api.openweathermap.org/data/2.5/weather?q=London&appid={api_key}'
    try:
        response = requests.get(test_url)
        if response.status_code == 401:
            return False, "Invalid API key"
        elif response.status_code == 200:
            return True, "API key is valid"
        else:
            return False, f"API error: {response.status_code}"
    except Exception as e:
        return False, f"Connection error: {e}"

def main():
    api_key = '8ce1cff6bd39610236ed7ab4b3ff45a1'
    
    print("Testing API key...")
    is_valid, message = test_api_key(api_key)
    if not is_valid:
        print(f"API Key Error: {message}")
        print("Please get a valid API key from https://openweathermap.org/api")
        print("1. Sign up for a free account")
        print("2. Go to 'My API Keys'")
        print("3. Copy your key and paste it in the code")
        return
    
    print("Automatically locating you...")
    city, region, country, lat, lon, timezone = get_location()
    if not city:
        print("Unable to get location.")
        return
    
    print(f"Detected location: {city}, {region}, {country}")
    print(f"Coordinates: Latitude {lat}, Longitude {lon}")
    print(f"Timezone: {timezone}")
    
    print("\nFetching current weather data...")
    current_data = get_current_weather_data(lat, lon, api_key)
    if not current_data or 'main' not in current_data:
        print("Unable to get current weather data.")
        if current_data:
            print(f"Response details: {current_data}")
        return
    
    print("Fetching forecast data...")
    forecast_data = get_forecast_data(lat, lon, api_key)
    
    tz = pytz.timezone(timezone)
    
    current = current_data['main']
    weather_info = current_data['weather'][0]
    wind_info = current_data.get('wind', {})
    sys_info = current_data.get('sys', {})
    
    temp = current.get('temp', 0)
    feels_like = current.get('feels_like', temp)
    temp_min = current.get('temp_min', temp)
    temp_max = current.get('temp_max', temp)
    pressure = current.get('pressure', 0)
    humidity = current.get('humidity', 0)
    visibility = current_data.get('visibility', 10000) / 1000 if current_data.get('visibility') else 10
    clouds = current_data.get('clouds', {}).get('all', 0)
    
    description = weather_info.get('description', 'Unknown').capitalize()
    wind_speed = wind_info.get('speed', 0)
    wind_deg = wind_info.get('deg')
    wind_dir = wind_direction(wind_deg)
    wind_gust = wind_info.get('gust', 'N/A')
    
    sunrise = datetime.fromtimestamp(sys_info.get('sunrise', 0), tz).strftime("%I:%M %p") if sys_info.get('sunrise') else 'N/A'
    sunset = datetime.fromtimestamp(sys_info.get('sunset', 0), tz).strftime("%I:%M %p") if sys_info.get('sunset') else 'N/A'
    local_time = datetime.now(tz).strftime("%B %d at %I:%M %p %Z")
    
    rain_1h = current_data.get('rain', {}).get('1h', 0)
    snow_1h = current_data.get('snow', {}).get('1h', 0)
    
    heat_index = calculate_heat_index(temp, humidity)
    wind_chill = calculate_wind_chill(temp, wind_speed)
    
    print(f"\n**Current Weather**")
    print(f"- Location: {description} in {city}, {region} for {local_time}")
    print(f"- Temperature: {temp:.1f}°C (feels like: {feels_like:.1f}°C)")
    print(f"- Min/Max: {temp_min:.1f}°C / {temp_max:.1f}°C")
    if heat_index:
        print(f"- Heat Index: {heat_index:.1f}°C")
    if wind_chill:
        print(f"- Wind Chill: {wind_chill:.1f}°C")
    print(f"- Humidity: {humidity}%")
    print(f"- Pressure: {pressure} hPa")
    print(f"- Visibility: {visibility:.1f} km")
    print(f"- Cloud Cover: {clouds}%")
    print(f"- Wind: {wind_speed:.1f} m/s from {wind_dir}")
    if wind_gust != 'N/A':
        print(f"- Wind Gust: {wind_gust} m/s")
    print(f"- Rain (last 1h): {rain_1h} mm")
    print(f"- Snow (last 1h): {snow_1h} mm")
    print(f"- Sunrise: {sunrise}")
    print(f"- Sunset: {sunset}")
    
    try:
        aqi, components = get_air_quality(lat, lon, api_key)
        if aqi:
            aqi_labels = {1: 'Good', 2: 'Fair', 3: 'Moderate', 4: 'Poor', 5: 'Very Poor'}
            health_recs = {
                1: 'Air quality is satisfactory.',
                2: 'Air quality is acceptable.',
                3: 'Members of sensitive groups may experience health effects.',
                4: 'Everyone may begin to experience health effects.',
                5: 'Health warnings of emergency conditions.'
            }
            print(f"- Air Quality: {aqi_labels.get(aqi, 'Unknown')} (AQI: {aqi})")
            print(f"- Health Recommendation: {health_recs.get(aqi, 'No recommendation available.')}")
    except:
        print("- Air Quality: Data not available in free tier")
    
    if forecast_data and 'list' in forecast_data:
        print(f"\n**5-Day Forecast (3-hour intervals)**")
        forecasts = forecast_data['list'][:40]
        
        current_day = None
        for forecast in forecasts:
            forecast_time = datetime.fromtimestamp(forecast['dt'], tz)
            forecast_day = forecast_time.strftime("%A, %B %d")
            
            if forecast_day != current_day:
                print(f"\n--- {forecast_day} ---")
                current_day = forecast_day
            
            time_str = forecast_time.strftime("%H:%M")
            temp_f = forecast['main']['temp']
            feels_f = forecast['main']['feels_like']
            desc_f = forecast['weather'][0]['description'].capitalize()
            pop_f = forecast.get('pop', 0) * 100
            rain_f = forecast.get('rain', {}).get('3h', 0)
            snow_f = forecast.get('snow', {}).get('3h', 0)
            wind_f = forecast['wind']['speed']
            wind_dir_f = wind_direction(forecast['wind'].get('deg'))
            
            print(f"  {time_str}: {temp_f:.1f}°C (feels {feels_f:.1f}°C), {desc_f}")
            print(f"     Precip: {pop_f:.0f}%, Rain: {rain_f}mm, Snow: {snow_f}mm, Wind: {wind_f:.1f}m/s {wind_dir_f}")

if __name__ == "__main__":
    main()
