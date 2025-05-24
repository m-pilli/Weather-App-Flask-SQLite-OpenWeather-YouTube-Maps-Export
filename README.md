# 🌦️ Weather Forecast App — Flask + SQLite + OpenWeather + YouTube

An interactive full-stack web app built using **Python Flask**, **SQLite**, and public APIs like **OpenWeatherMap** and **YouTube Data API**. This application lets users search for real-time weather in any city, view a 5-slot forecast, watch related YouTube videos, see the location on Google Maps, and manage search history with full CRUD support. Users can also export their data as CSV or JSON.

## Features
- 🌤 Real-time current weather and 5-time-slot forecast
- 🎥 YouTube video suggestions for the searched city
- 🗺️ Google Maps integration
- 💾 SQLite-backed search history
- ✏️ Full CRUD: Create, Read, Update, Delete
- 📤 Export search history to CSV and JSON
- 💅 Animated and responsive UI

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/weather-app.git
cd weather-app
```

### 2. Create and Activate Virtual Environment (optional)
```bash
python -m venv venv
venv\Scripts\activate  # For Windows
# OR
source venv/bin/activate  # For macOS/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create a `.env` File
Create a `.env` file in the root directory and add:
```
WEATHER_API_KEY=your_openweather_api_key
YOUTUBE_API_KEY=your_youtube_api_key
```

### 5. Run the App
```bash
python app.py
```
Visit: `http://localhost:5000` in your browser

## Notes
- Keep your `.env` file private. It should be listed in `.gitignore`.
- The database (`weather.db`) is auto-created locally.

## Author
Mahathi Pilli  
Graduate Student — Computer Science @ Texas State University
