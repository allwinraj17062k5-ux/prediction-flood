import streamlit as st
import requests
import folium
from streamlit_folium import st_folium
import numpy as np

# Page config
st.set_page_config(page_title="Flood Risk Prediction", layout="wide")

# Title
st.title("🌊 Flood Risk Prediction System")
st.write("Predict flood risk using real-time weather data.")

# Sidebar input
st.sidebar.header("Location Input")

lat = st.sidebar.number_input("Latitude", value=13.0827)
lon = st.sidebar.number_input("Longitude", value=80.2707)

# Default values
temp = 0
wind = 0

# Weather API URL
url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m"

try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        data = response.json()

        if "current" in data:
            temp = data["current"].get("temperature_2m", 0)
            wind = data["current"].get("wind_speed_10m", 0)
        else:
            st.warning("Weather data not available from API")

    else:
        st.error(f"Weather API error (Status code: {response.status_code})")

except requests.exceptions.RequestException as e:
    st.error(f"Connection error: {e}")

# Simulated rainfall
rainfall = np.random.randint(0, 200)

# Flood risk logic
if rainfall > 120 or wind > 40:
    risk = "High Flood Risk 🔴"
elif rainfall > 70:
    risk = "Moderate Flood Risk 🟠"
else:
    risk = "Low Flood Risk 🟢"

# Weather display
st.subheader("Current Weather Data")

col1, col2, col3 = st.columns(3)

col1.metric("Temperature (°C)", temp)
col2.metric("Wind Speed (km/h)", wind)
col3.metric("Rainfall (mm)", rainfall)

# Prediction result
st.subheader("Flood Risk Prediction")
st.success(risk)

# Map
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
st.write("Developed using Streamlit and Open-Meteo API")
