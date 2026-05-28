import sqlite3

class DBService:
    def __init__(self):
        print(sqlite3.sqlite_version)
        self.conn = sqlite3.connect("app.db")
        self.cursor = self.conn.cursor()

    def setup(self):
        self.cursor.execute("""
            PRAGMA foreign_keys = ON;
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(255) UNIQUE,
                duration TEXT
            );
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_id INTEGER,
                session_seconds INTEGER,
                pause_seconds INTEGER,
                date TEXT,
                FOREIGN KEY(job_id) references jobs(id) ON DELETE CASCADE
            );
        """)
        self.conn.commit()
    
    def insert_job(self, job):
        name, duration = list(job)
        self.cursor.execute(
            "INSERT INTO jobs (name, duration) VALUES (?,?) on CONFLICT(name) DO UPDATE SET duration = excluded.duration;",
            (name, duration)
        )
        self.conn.commmit()
    
    