from services.database.database_service import DatabaseService
from services.time_services import TimeService
from dataclasses import dataclass, field
import time

@dataclass
class AppState:
    currentDate: str = ""
    currentJob: str = ""
    labels_for_jobs: list[str] = field(default_factory=list)
    job_durations: dict[str, str] = field(default_factory=dict)
    running_job: bool = False
    running_pause: bool = False
    elapsed_seconds: int = 0
    session_job_seconds: int= 0
    session_pause_seconds: int = 0
    currentSession: str = ""
    totalTime: str = ""
    todaysTotalTime: str = ""

    def setup(self):
        time_service = TimeService()
        db = DatabaseService()
        db.setup()
        self.currentDate =  time.strftime("%Y-%m-%d")
        self.job_durations = db.get_all_jobs()
        self.labels_for_jobs = db.get_job_labels()
        #time_service.get_total_time()
        self.totalTime =  "01:23:45"
        self.todaysTotalTime = "00:00:00"
        self.currentJob = "Devops"

        self.currentSession = "00:00:00"

        self.running_job = False
        self.running_pause = False
        self.session_job_seconds = 0
        self.session_pause_seconds = 0


        


            

