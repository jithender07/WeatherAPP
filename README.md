Weather App README

Overview
This Weather App fetches and displays current weather information for a specified city using the OpenWeatherMap API. The application is written in Python and uses the `requests` library to make HTTP requests to the API.

 Features
- Fetches real-time weather data for any city in the world.
- Displays:
  - City name
  - Temperature (in Fahrenheit)
  - Weather description
  - Humidity percentage
  - Wind speed (in meters per second)

Prerequisites
- Python 3.x installed on your system
- An active internet connection
- An API key from OpenWeatherMap

Setup Instructions

1. Clone or Download the Repository
   Download the Python script or clone this repository to your local machine.

2. Install Dependencies
   Ensure the `requests` library is installed. You can install it using pip:
   ```bash
   pip install requests
   ```

3. Obtain an API Key
   - Visit [OpenWeatherMap](https://openweathermap.org/api) and sign up for a free account.
   - Generate an API key.
   - Replace the `API_KEY` value in the script with your own API key.

4. Run the Script
   Execute the script using Python:
   ```bash
   python weather_app.py
   ```
   
5. Enter a City Name
   When prompted, enter the name of a city to get its current weather data.

 Example Usage
```bash
Enter City: New York
City: New York
Temperature: 72°F
Weather: clear sky
Humidity: 55%
Wind Speed: 3 m/s
```

Error Handling
- If the entered city is not found or there is an issue with the API request, the script will display:
  ```
  Error fetching weather data.
  ```

 Customization
- Units: By default, the script fetches temperature data in Fahrenheit. To change this:
  - Replace `'units': 'imperial'` with `'units': 'metric'` (for Celsius).
- Language: Add a `'lang': '<language_code>'` parameter in the API request to fetch weather descriptions in a specific language. For example:
  ```python
  'lang': 'es'  # for Spanish
  ```

Notes
- The script assumes the API key is valid. Make sure to keep your API key secure and do not share it publicly.
- OpenWeatherMap free tier limits the number of API requests per minute. Refer to their documentation for more details.




