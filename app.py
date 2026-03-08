import streamlit as st
import pandas as pd
import requests
import folium
from streamlit_folium import st_folium
import numpy as np

st.set_page_config(page_title="Flood Risk Prediction", layout="wide")

st.title("🌊 Flood Risk Prediction System")
st.write("Predict flood risk using real-time weather data.")

# Sidebar inputs
st.sidebar.header("Location Input")

lat = st.sidebar.number_input("Latitude", value=13.0827)
lon = st.sidebar.number_input("Longitude", value=80.2707)

# Weather API
url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

try:
    response = requests.get(url)
    data = response.json()

    if "current_weather" in data:
        temp = data["current_weather"]["temperature"]
        wind = data["current_weather"]["windspeed"]
    else:
        temp = 0
        wind = 0
        st.warning("Weather data not available")

except:
    temp = 0
    wind = 0
    st.error("Failed to fetch weather data")

# Simulated rainfall (for demo)
rainfall = np.random.randint(0, 200)

# Flood risk logic
if rainfall > 120 or wind > 40:
    risk = "High Flood Risk 🔴"
elif rainfall > 70:
    risk = "Moderate Flood Risk 🟠"
else:
    risk = "Low Flood Risk 🟢"

# Display weather
st.subheader("Current Weather Data")

col1, col2, col3 = st.columns(3)

col1.metric("Temperature (°C)", temp)
col2.metric("Wind Speed (km/h)", wind)
col3.metric("Rainfall (mm)", rainfall)

# Flood result
st.subheader("Flood Risk Prediction")
st.success(risk)

# Map display
st.subheader("Location Map")

m = folium.Map(location=[lat, lon], zoom_start=10)

folium.Marker(
    [lat, lon],
    popup=risk,
    tooltip="Selected Location"
).add_to(m)

st_folium(m, width=700)

# Footer
st.markdown("---")
st.write("Developed using Streamlit and Open Meteo API")
