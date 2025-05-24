# Weather-App-Flask-SQLite-YouTube-OpenWeather
A full-stack weather app built with Flask and SQLite that fetches real-time weather data and a 5-time forecast using OpenWeather API. It integrates with the YouTube Data API to show city-specific videos and supports full CRUD operations with a search history database.


# 🌦️ Weather Forecast App — Flask + SQLite + OpenWeather + YouTube

A beautiful, full-stack **weather forecast web app** built with **Python Flask** that shows **real-time weather**, a **5-slot forecast**, and **relevant YouTube travel videos** for any searched location.  
It also features a **search history** with full **CRUD support**, animated UI, and clean design — perfect to showcase full-stack and UI/UX skills.

---

## 🎨 Fonts & Styling

- Font: [Inter](https://fonts.google.com/specimen/Inter) (via Google Fonts)
- Theme: Light mode with pastel accents
- Effects: CSS animations (fade-in, pop-in, slide), hover glows, responsive UI

---

## 🚀 Features

- 🔍 **Search weather by city name** (current + forecast)
- 📅 **5-slot weather forecast** using OpenWeatherMap
- 🎥 **YouTube video suggestions** for the city
- 💾 **Search history** saved in local SQLite database
- 🛠️ **CRUD operations**:
  - Create (save search)
  - Read (view history)
  - Update (edit entries)
  - Delete (remove entries)
- 💅 Interactive UI with transitions, effects, and accessible layout

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/YOUR_USERNAME/weather-app.git
cd weather-app

2 . Create a Virtual Environment (optional but recommended)

python -m venv venv
venv\Scripts\activate      # Windows
# OR
source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Create a .env File

Create a .env file in the root directory and add:

WEATHER_API_KEY=your_openweather_api_key
YOUTUBE_API_KEY=your_youtube_api_key

5. Run the App

python app.py

Visit: http://localhost:5000 in your browser

Notes

Keep your .env file private. It should be listed in .gitignore.

The database (weather.db) is auto-created locally.
