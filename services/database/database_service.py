import sqlite3

class DatabaseService:
    def __init__(self):
        self.conn = sqlite3.connect("app.db")
        self.cursor = self.conn.cursor()

    def setup(self):
        #self.reset_tables()
        self.cursor.execute("PRAGMA foreign_keys = ON;")
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS weeks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                week_start TEXT UNIQUE
            );
        """)
        self.cursor.execute("""            
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                week_id INTEGER,
                name VARCHAR(255) UNIQUE,
                duration TEXT,
                current_date TEXT,
                FOREIGN KEY(week_id) references weeks(id)
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

    def update_weeks_table(self, date):
        #only update the weeks table if date is not found in table 
        self.cursor.execute("""
            INSERT INTO weeks (week_start)
            VALUES (?)
            ON CONFLICT(week_start) DO NOTHING; 
        """,(date,)
        )
        self.conn.commit()   

    def get_week_id(self, date):
        self.cursor.execute(
            "SELECT id FROM weeks WHERE week_start = ?",
            (date,)
        )
        return self.cursor.fetchone()[0]

    def insert_job(self, job):
        name, duration, start_of_week, current_date = job
        week_id = self.get_week_id(start_of_week)
        self.cursor.execute(
            "INSERT INTO jobs (name, duration, week_id, current_date) " \
            "VALUES (?,?,?,?) " \
            "on CONFLICT(name) DO UPDATE SET duration = excluded.duration;", 
            (name, duration, week_id, current_date)
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

    def get_todays_jobs(self, today):
        #get week_id first by get the start week associated to today
        #start_week = get_start_week(today)
        '''
        start_week = week_service.get_start_of_week(today)
        week_id = self.get_week_id(start_week)
        self.cursor.execute("SELECT name, duration FROM jobs WHERE week_id = ?",(week_id,))
        all_jobs = {}
        for i, item in enumerate(self.cursor.fetchall()):
            job, duration = item
            all_jobs[job] = duration 
        return all_jobs
'''
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
    
    def update_jobs(self, state):
        #while comparing deletedList
        self.cursor.execute("PRAGMA foreign_keys = ON;")
        for job, duration in state.deleted_jobs.items():
            self.cursor.execute("DELETE FROM jobs WHERE name=?", (job,))
        self.conn.commit()

    def get_weeks(self):
        self.cursor.execute("SELECT * FROM weeks")
        return self.cursor.fetchall()
    
    def get_all_jobs(self, weeks):
        #using weeks, go through each job, adding to all_jobs such that
        #   all_jobs is a list, each item in the list groups jobs by week_date
        all_jobs = []
        
        for week in weeks:
            print("week : ", week)
            week_id, date = list(week)
            self.cursor.execute("SELECT name, duration, current_date FROM jobs WHERE week_id = ?",
            (week_id,))
            result = self.cursor.fetchall()

            jobs_in_week = {}
            for job in result:
                name, duration, current_date = job
                jobs_in_week["name"] = name
                jobs_in_week["duration"] = duration
                jobs_in_week["current_date"] = current_date
            all_jobs.append(jobs_in_week)
        return all_jobs
        
    def reset_tables(self):
        self.cursor.execute("DROP TABLE weeks")
        self.cursor.execute("DROP TABLE jobs")
        self.cursor.execute("DROP TABLE sessions")
        self.conn.commit()