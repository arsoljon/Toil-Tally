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
        name, duration = job
        self.cursor.execute(
            "INSERT INTO jobs (name, duration) " \
            "VALUES (?,?) " \
            "on CONFLICT(name) DO UPDATE SET duration = excluded.duration;", 
            (name, duration)
        )
        self.conn.commit()
    
    def insert_session(self, state):
        self.cursor.execute("SELECT id FROM jobs WHERE name=?",(state.currentJob,))
        job_id = self.cursor.fetchone()[0]
        seconds_session = state.session_job_seconds
        date = state.currentDate
        self.cursor.execute(
            "INSERT INTO sessions (job_id, session_seconds, date) " \
            "VALUES (?,?,?) ",
            (job_id, seconds_session, date,)
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
    
    def get_total_sessions_by_date(self, date):
        self.cursor.execute("SELECT session_seconds FROM sessions WHERE date=?",(date,))
        total_seconds = 0
        for i, session in enumerate(self.cursor.fetchall()):
            total_seconds += session[0]
        return total_seconds 
    
    def update_jobs(self, controller, state):
        #while comparing deletedList
        for job, duration in controller.deleted_jobs.items():
            self.cursor.execute("DELETE FROM jobs WHERE name=?", (job,))
        self.conn.commit()

    def reset_tables(self):
        self.cursor.execute("DROP TABLE jobs")
        self.cursor.execute("DROP TABLE sessions")
        self.conn.commit()