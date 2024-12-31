import requests

API_KEY = '934b12243c125176c221dff0074d5101'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def weather(city):
    response = requests.get(BASE_URL, params = {
        'q': city,
        'appid': API_KEY,
        'units': 'imperial'
    })
    if response.status_code==200:
        return response.json()
    else:
        return  None

Input = input("Enter City")
weather_data = weather(Input)
if weather_data:
    print(f"City: {weather_data['name']}")
    print(f"Temperature: {weather_data['main']['temp']}°F")
    print(f"Weather: {weather_data['weather'][0]['description']}")
    print(f"Humidity: {weather_data['main']['humidity']}%")
    print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
else:
    print("Error fetching weather data.")

