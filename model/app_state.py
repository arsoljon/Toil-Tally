from services.database.database_service import DatabaseService
from services.state_service import StateService
from services.week_service import WeekService
from dataclasses import dataclass, field
import time

@dataclass
class AppState:
    currentDate: str = ""
    currentJob: str = ""
    labels_for_jobs: list[str] = field(default_factory=list)
    job_durations: dict[str, str] = field(default_factory=dict)
    deleted_jobs: dict[str, str] = field(default_factory=dict)
    running_job: bool = False
    running_pause: bool = False
    elapsed_seconds: int = 0
    session_job_seconds: int= 0
    session_pause_seconds: int = 0
    session_initial: int = 0
    session_current: int = 0
    totalTime: str = ""
    todaysTotalTime: str = ""
    start_of_week: str = ""
    job_count: int = 0
    hours_this_week: str = ""
    avg_per_day: str = ""
    top_job: str = "" 


    def setup(self):
        state_service = StateService()
        week_service = WeekService()
        
        db = DatabaseService()
        db.setup()
        self.currentDate =  time.strftime("%Y-%m-%d")
        self.job_durations = db.get_all_jobs()
        self.labels_for_jobs = db.get_job_labels()
        self.totalTime = state_service.get_total_time(self.job_durations)
        self.todaysTotalTime = state_service.get_todays_total_time(self.currentDate)
        self.currentJob = ""

        self.session_initial = 0
        self.session_current = 0

        self.running_job = False
        self.running_pause = False
        self.session_job_seconds = 0
        self.session_pause_seconds = 0

        self.deleted_jobs = {}

        self.start_of_week = week_service.get_start_of_week(self.currentDate)
        self.job_count = week_service.get_job_count(self.job_durations)
        self.hours_this_week = week_service.get_total_hours(self.job_durations)
        self.avg_per_day = week_service.get_avg_per_day(self.job_durations)
        self.top_job = week_service.get_top_job(self.job_durations)

        self.all_weeks = state_service.get_all_weeks()
        self.column_labels = state_service.get_labels(self.all_weeks[0])
        #self.all_weeks = week_service.get_all_weeks()
            

