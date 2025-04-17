import streamlit as st
import requests

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