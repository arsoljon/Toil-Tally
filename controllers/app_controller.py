from services.delete_service import DeleteService
from services.state_service import StateService
from services.status_service import StatusService
from services.time_services import TimeService
from services.week_service import WeekService
import time
from services.database.database_service import DatabaseService

class AppController:
    def __init__(self):
        self.db = DatabaseService()
        self.week_service = WeekService()
        self.time_service = TimeService()
        self.status_service = StatusService()
        self.state_service = StateService()
        self.delete_service = DeleteService()

    def setup_db(self, db):
        db.setup()

    def setup_state(self, state):
        state.currentDate =  time.strftime("%Y-%m-%d")
        #state.currentDate = "2026-05-20"
        state.job_durations = self.db.get_todays_jobs(state.currentDate)
        state.labels_for_jobs = self.db.get_job_labels()
        state.totalTime = self.state_service.get_total_time(state.job_durations)
        state.todaysTotalTime = self.state_service.get_todays_total_time(state.currentDate)
        state.currentJob = ""

        state.session_initial = 0
        state.session_current = 0

        state.running_job = False
        state.running_pause = False
        state.session_job_seconds = 0
        state.session_pause_seconds = 0

        state.deleted_jobs = {}

        state.start_of_week = self.week_service.get_start_of_week(state.currentDate)
        state.job_count = self.week_service.get_job_count(state.job_durations)
        state.hours_this_week = self.week_service.get_total_hours(state.job_durations)
        state.avg_per_day = self.week_service.get_avg_per_day(state.job_durations)
        state.top_job = self.week_service.get_top_job(state.job_durations)

        state.all_weeks = self.state_service.get_all_weeks()
        state.column_labels = self.state_service.get_labels(state.all_weeks[0])
        #state.all_weeks = week_service.get_all_weeks()