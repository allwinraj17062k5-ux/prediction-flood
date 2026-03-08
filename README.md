# 🌊 Tamil Nadu AI Disaster Monitoring System

## 📌 Project Overview

The **Tamil Nadu AI Disaster Monitoring System** is a web-based dashboard that monitors weather conditions and predicts potential flood risk using Artificial Intelligence. The system collects real-time weather data (temperature, wind speed, and rainfall) and applies a simple LSTM deep learning model to estimate flood probability.

The dashboard displays disaster information through an interactive map, district-level metrics, and visual charts. This project demonstrates how AI and real-time data can support disaster management systems.

---

## 🚀 Features

* Real-time weather data retrieval using API
* AI-based flood prediction using LSTM deep learning
* Tamil Nadu district disaster monitoring
* Interactive map showing selected district risk
* District-wise disaster heatmap visualization
* Automatic resource estimation (boats and emergency equipment)
* Mobile-friendly dashboard interface

---

## 🛠 Technologies Used

* **Python**
* **Streamlit** – Web application framework
* **TensorFlow / Keras** – AI model implementation
* **Pandas & NumPy** – Data processing
* **Folium** – Interactive map visualization
* **Open-Meteo API** – Real-time weather data

---

## 🤖 AI Model

The system uses a **Long Short-Term Memory (LSTM)** neural network to estimate flood risk.

### Input Features

* Temperature
* Wind Speed
* Rainfall

### Output

* Flood Risk Level (Low / High)

The model is trained using sample weather patterns and predicts flood probability for the selected district.

---

## 🗺 System Workflow

1. User selects a district in Tamil Nadu.
2. The system fetches live weather data using the Open-Meteo API.
3. The AI model processes temperature, wind, and rainfall data.
4. The model predicts the flood risk level.
5. The dashboard displays:

   * Weather metrics
   * Flood risk prediction
   * Required emergency resources
   * District location on the disaster map
   * Heatmap chart for district risk comparison.

---

## 📊 Dashboard Components

* Weather Monitoring Panel
* AI Flood Prediction Module
* Disaster Resource Allocation
* Interactive District Map
* District Disaster Heatmap

---

## 🌐 Deployment

The application is deployed using **Streamlit Community Cloud**.

Live Application:
https://your-app-name.streamlit.app

---

## 🎓 Project Purpose

This project demonstrates how **Artificial Intelligence, geospatial visualization, and real-time weather data** can be combined to build a disaster monitoring dashboard. Such systems can assist authorities in early warning and disaster response planning.

---

