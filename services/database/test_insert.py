import sqlite3

conn = sqlite3.connect("app.db")
cursor = conn.cursor()

cursor.execute(
    "INSERT INTO jobs (name) VALUES (?)",
    ("Developer",)
)

conn.commit()
conn.close()