import streamlit as st
import pandas as pd
import requests
import folium
from streamlit_folium import st_folium
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

st.set_page_config(layout="wide")

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

# -------- SATELLITE RAINFALL DATA --------

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

# -------- LSTM AI MODEL --------

# sample training data
X = np.array([
[20,5,0],
[25,6,1],
[30,10,5],
[35,15,10],
[40,20,20],
[45,25,30]
])

y = np.array([0,0,0,1,1,1])

X = X.reshape((X.shape[0],1,X.shape[1]))

model = Sequential()
model.add(LSTM(10, activation='relu', input_shape=(1,3)))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy')

model.fit(X,y,epochs=50,verbose=0)

test = np.array([[temp,wind,rain]])
test = test.reshape((1,1,3))

prediction = model.predict(test)

st.subheader("🤖 AI Flood Prediction")

if prediction[0][0] > 0.5:
    risk = "HIGH FLOOD RISK"
    boats = 15
    equipment = 40
else:
    risk = "LOW FLOOD RISK"
    boats = 4
    equipment = 10

st.write("Risk Level:", risk)

st.write("Boats Required:", boats)
st.write("Emergency Equipment:", equipment)

# -------- DISTRICT BOUNDARY MAP --------

st.subheader("🗺 Tamil Nadu Disaster Map")

m = folium.Map(location=[11,78], zoom_start=7)

folium.Marker(
location=[lat,lon],
popup=f"{district} Risk: {risk}",
icon=folium.Icon(color="red")
).add_to(m)

st_folium(m, width=900, height=500)

# -------- DISTRICT HEATMAP --------

st.subheader("🔥 District Disaster Heatmap")

heat_data = pd.DataFrame({
"district": list(districts.keys()),
"risk":[20,40,35,60,50,45]
})

st.bar_chart(heat_data.set_index("district"))
