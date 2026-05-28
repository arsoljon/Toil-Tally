import sqlite3

class DatabaseService:
    def __init__(self):
        self.conn = sqlite3.connect("app.db")
        self.cursor = self.conn.cursor()

    def setup(self):
        #self.reset_tables()
        self.cursor.execute("PRAGMA foreign_keys = ON;")
        self.cursor.execute("""            
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(255) UNIQUE,
                duration TEXT
            );
        """)
        self.cursor.execute("""
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

    def get_job_duration(self):
        pass

    def insert_job(self, job):
        name, duration = list(job)
        self.cursor.execute(
            "INSERT INTO jobs (name, duration) " \
            "VALUES (?,?) " \
            "on CONFLICT(name) DO UPDATE SET duration = excluded.duration;", 
            (name, duration)
        )
        self.conn.commit()

    def get_total_time(self):
        #add durations for all jobs
        self.cursor.execute(
            "SELECT duration FROM jobs"
        )
        print(self.cursor.fetchall())

    def get_todays_total_time(self, state):
        #add durations from all todays sessions
        pass

    def get_all_jobs(self):
        self.cursor.execute("SELECT name, duration FROM jobs")
        all_jobs = {}
        for i, item in enumerate(self.cursor.fetchall()):
            job, duration = item
            all_jobs[job] = duration 
        return all_jobs

    def get_job_labels(self):
        self.cursor.execute("SELECT name FROM jobs")
        all_labels = []
        for i, labels in enumerate(self.cursor.fetchall()):
            all_labels.append(labels[0])
        return all_labels
    
    def reset_tables(self):
        self.cursor.execute("DROP TABLE jobs")
        self.cursor.execute("DROP TABLE sessions")
        self.conn.commit()