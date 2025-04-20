import streamlit as st
import requests
import datetime

API_KEY = "2c72c80c241e422dbc0163855251604"
BASE_URL = "http://api.weatherapi.com/v1"

# Set the title of the Streamlit app
st.title("What's the vibe outside today?")

# Ask the user for a city name
city = st.text_input("Drop the city name")

# If the user has entered a city name
if city:
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

        # Display location
        st.subheader(f"{city}, {region}, {country}")
        st.caption(f"Local time: {time}")
        st.markdown("---")

        # Weather details in columns
        col1, col2, col3 = st.columns(3)
        col1.metric("Temperature", f"{temperature}°F", f"Feels like {feel}°F")
        col2.metric("Humidity", f"{humidity}%")
        col3.metric("Condition", condition)

        # Vibe slider
        st.markdown("---")
        vibe = st.slider("Rate the vibe today based on the weather", 1, 10)
        st.write(f"The vibe is a {vibe}/10")

    else:
        st.error("Error: Unable to fetch weather data. Please try a different city.")

    # Get yesterday's date
    yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")

    # Full API request url to get yesterday's weather data
    past_endpoint = f"{BASE_URL}/history.json?key={API_KEY}&q={city}&dt={yesterday}"
    past_response = requests.get(past_endpoint)  # Send a GET request to the API

    # Check if the request was successful
    if past_response.status_code == 200:
        past_data = past_response.json()  # convert the response to JSON

        # Extract yesterday's weather details
        past_temperature = past_data['forecast']['forecastday'][0]['day']['avgtemp_f']

        # Compare today's and yesterday's temperature
        temperature_difference = round(temperature - past_temperature, 1)
        
        if temperature_difference > 0:
            st.success(f"It's {temperature_difference}°F warmer today than yesterday!")
        elif temperature_difference < 0:
            st.warning(f"It's {abs(temperature_difference)}°F cooler today than yesterday.")
        else:
            st.info("The temperature is the same as yesterday.")
    else:
        st.error("Error: Unable to fetch yesterday's weather data. Please try again later.")