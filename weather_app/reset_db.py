import sqlite3

conn = sqlite3.connect('weather.db')
cursor = conn.cursor()

# Delete all rows
cursor.execute("DELETE FROM weather")

# Reset ID counter
cursor.execute("DELETE FROM sqlite_sequence WHERE name='weather'")

conn.commit()
conn.close()
print("✅ Weather table cleared and ID reset.")
