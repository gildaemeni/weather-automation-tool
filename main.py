import requests

API_KEY = "2c72c80c241e422dbc0163855251604"
BASE_URL = "http://api.weatherapi.com/v1"

# Ask the user for a city name
city = input("Enter the city name: ")

# Full API request url to get the weather data of city
endpoint = f"{BASE_URL}/current.json?key={API_KEY}&q={city}"
response = requests.get(endpoint)  # Send a GET request to the API

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # convert the response to JSON

    # Extract the location details
    city = data['location']['name']
    region = data['location']['region']
    country = data['location']['country']
    time = data['location']['localtime']

    # Extract real-time weather details
    temperature = data['current']['temp_f']
    condition = data['current']['condition']['text']
    humidity = data['current']['humidity']
    feel = data['current']['feelslike_f']

    # Format the weather report
    weather_report = (
        f"City: {city}\n"
        f"Region: {region}\n"
        f"Country: {country}\n"
        f"Time: {time}\n"
        f"Temperature: {temperature}°F\n"
        f"Condition: {condition}\n"
        f"Humidity: {humidity}%\n"
        f"Feels Like: {feel}°F\n"
    )

    print(weather_report) # display the weather report

else:
    print("Error: Unable to fetch weather data.")