import streamlit as st
import requests
import folium
from streamlit_folium import st_folium
import numpy as np

st.set_page_config(page_title="Flood Risk Prediction", layout="wide")

st.title("🌊 Flood Risk Prediction System")
st.write("Predict flood risk using weather data.")

# Tamil Nadu districts with coordinates
districts = {
    "Chennai": [13.0827, 80.2707],
    "Coimbatore": [11.0168, 76.9558],
    "Madurai": [9.9252, 78.1198],
    "Salem": [11.6643, 78.1460],
    "Tiruchirappalli": [10.7905, 78.7047],
    "Erode": [11.3410, 77.7172],
    "Vellore": [12.9165, 79.1325],
    "Tirunelveli": [8.7139, 77.7567]
}

st.sidebar.header("Select Location")

district = st.sidebar.selectbox("Choose District", list(districts.keys()))

lat, lon = districts[district]

# store values so they don't reset
if "temp" not in st.session_state:
    st.session_state.temp = 0
if "wind" not in st.session_state:
    st.session_state.wind = 0

if st.sidebar.button("Get Weather Data"):

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()

            if "current_weather" in data:
                st.session_state.temp = data["current_weather"]["temperature"]
                st.session_state.wind = data["current_weather"]["windspeed"]

            else:
                st.warning("Weather data not available")

        else:
            st.error("Weather API error")

    except:
        st.error("Connection error")


# simulated rainfall
rainfall = np.random.randint(0, 200)

temp = st.session_state.temp
wind = st.session_state.wind

# flood logic
if rainfall > 120 or wind > 40:
    risk = "High Flood Risk 🔴"
elif rainfall > 70:
    risk = "Moderate Flood Risk 🟠"
else:
    risk = "Low Flood Risk 🟢"


st.subheader("Current Weather Data")

col1, col2, col3 = st.columns(3)

col1.metric("Temperature (°C)", temp)
col2.metric("Wind Speed (km/h)", wind)
col3.metric("Rainfall (mm)", rainfall)


st.subheader("Flood Risk Prediction")
st.success(risk)


st.subheader("Location Map")

m = folium.Map(location=[lat, lon], zoom_start=9)

folium.Marker(
    [lat, lon],
    popup=district,
    tooltip=district
).add_to(m)

st_folium(m, width=700)

st.markdown("---")
st.write("Developed using Streamlit and Open Meteo API")
