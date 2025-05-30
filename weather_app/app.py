from flask import Flask, render_template, request, Response
import requests
import os
import sqlite3
import json
import csv
from dotenv import load_dotenv
from database import init_db

load_dotenv()
init_db()

app = Flask(__name__)
API_KEY = os.getenv("WEATHER_API_KEY")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

def get_youtube_videos(query):
    url = f"https://www.googleapis.com/youtube/v3/search"
    params = {
        'part': 'snippet',
        'q': f"{query} travel",
        'key': YOUTUBE_API_KEY,
        'maxResults': 3,
        'type': 'video'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        videos = response.json().get("items", [])
        return [f"https://www.youtube.com/watch?v={v['id']['videoId']}" for v in videos]
    return []

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    forecast = None
    error = None
    youtube_links = []

    if request.method == 'POST':
        city = request.form['city']
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather = {
                'city': city,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon']
            }

            forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
            forecast_response = requests.get(forecast_url)
            if forecast_response.status_code == 200:
                forecast = forecast_response.json()['list'][:5]

            conn = sqlite3.connect('weather.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO weather (city, date, temperature, description)
                VALUES (?, date('now'), ?, ?)
            ''', (city, data['main']['temp'], data['weather'][0]['description']))
            conn.commit()
            conn.close()

            youtube_links = get_youtube_videos(city)
        else:
            error = "City not found. Try again!"

    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM weather ORDER BY id DESC")
    records = cursor.fetchall()
    conn.close()

    return render_template("index.html", weather=weather, forecast=forecast, error=error, records=records, youtube_links=youtube_links)

@app.route('/delete/<int:id>')
def delete_record(id):
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM weather WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return '<script>window.location="/";</script>'

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_record(id):
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        city = request.form['city']
        date = request.form['date']
        temperature = request.form['temperature']
        description = request.form['description']

        cursor.execute('''
            UPDATE weather
            SET city = ?, date = ?, temperature = ?, description = ?
            WHERE id = ?
        ''', (city, date, temperature, description, id))
        conn.commit()
        conn.close()
        return '<script>window.location="/";</script>'

    cursor.execute("SELECT * FROM weather WHERE id = ?", (id,))
    record = cursor.fetchone()
    conn.close()
    return render_template("edit.html", record=record)

@app.route('/export/csv')
def export_csv():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM weather")
    rows = cursor.fetchall()
    conn.close()

    csv_data = "ID,City,Date,Temperature,Description\n"
    for r in rows:
        csv_data += f"{r[0]},{r[1]},{r[2]},{r[3]},{r[4]}\n"

    return Response(
        csv_data,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=weather_export.csv"}
    )

@app.route('/export/json')
def export_json():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM weather")
    rows = cursor.fetchall()
    conn.close()

    data = [
        {"id": r[0], "city": r[1], "date": r[2], "temperature": r[3], "description": r[4]}
        for r in rows
    ]

    return Response(
        json.dumps(data, indent=4),
        mimetype="application/json",
        headers={"Content-Disposition": "attachment;filename=weather_export.json"}
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')