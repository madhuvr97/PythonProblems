import requests
from projects_low_complexity.secrets import get_secrets

def fetch_weather(city):
    secrets = get_secrets()
    api_key = secrets['api_key']
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    try:
        response = requests.get(base_url)
        data = response.json()

        if data['cod'] == 200:
            weather_info = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }
            return weather_info
        else:
            return None
    except Exception as e:
        print("Error:", e)
        return None

def main():
    city = input("Enter the city name: ").lower()
    weather = fetch_weather(city)

    if weather:
        print(f"Weather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Description: {weather['description']}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        print("Failed to fetch weather data. Please check the city name and try again.")

if __name__ == "__main__":
    main()

