import streamlit as st
import pandas as pd
import requests
import folium
from streamlit_folium import st_folium
import numpy as np

st.set_page_config(layout="wide", page_title="Tamil Nadu Disaster AI", page_icon="🌊")

st.title("🌊 Tamil Nadu AI Disaster Monitoring System")
st.markdown("Real-time flood prediction using satellite rainfall + AI")

# Tamil Nadu districts with coordinates
districts = {
    "Chennai": (13.0827,80.2707),
    "Coimbatore": (11.0168,76.9558),
    "Madurai": (9.9252,78.1198),
    "Salem": (11.6643,78.1460),
    "Trichy": (10.7905,78.7047),
    "Tirunelveli": (8.7139,77.7567)
}

district = st.selectbox("Select District", list(districts.keys()))

lat, lon = districts[district]

# -------- REAL WEATHER DATA --------

url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=rain&current_weather=true"

data = requests.get(url).json()

temp = data["current_weather"]["temperature"]
wind = data["current_weather"]["windspeed"]

try:
    rain = data["hourly"]["rain"][0]
except:
    rain = 0

col1, col2, col3 = st.columns(3)

col1.metric("Temperature °C", temp)
col2.metric("Wind km/h", wind)
col3.metric("Rainfall mm", rain)

# -------- AI FLOOD PREDICTION LOGIC --------

st.subheader("🤖 AI Flood Prediction")

# simple AI rule-based logic
if rain > 20 or wind > 25:
    prediction = 0.8
elif rain > 10:
    prediction = 0.6
else:
    prediction = 0.2

if prediction > 0.6:
    risk = "HIGH FLOOD RISK"
    boats = 15
    equipment = 40
elif prediction > 0.4:
    risk = "MODERATE FLOOD RISK"
    boats = 8
    equipment = 20
else:
    risk = "LOW FLOOD RISK"
    boats = 2
    equipment = 5

st.write("Risk Level:", risk)
st.write("Boats Required:", boats)
st.write("Emergency Equipment:", equipment)

# -------- DISASTER MAP --------

st.subheader("🗺 Tamil Nadu Disaster Map")

m = folium.Map(location=[11,78], zoom_start=7)

color = "green"

if risk == "MODERATE FLOOD RISK":
    color = "orange"

if risk == "HIGH FLOOD RISK":
    color = "red"

folium.Marker(
    location=[lat,lon],
    popup=f"{district} Risk: {risk}",
    icon=folium.Icon(color=color, icon="info-sign")
).add_to(m)

st_folium(m, width=900, height=500)

# -------- DISTRICT HEATMAP --------

st.subheader("🔥 District Disaster Heatmap")

heat_data = pd.DataFrame({
    "district": list(districts.keys()),
    "risk":[20,40,35,60,50,45]
})

st.bar_chart(heat_data.set_index("district"))
