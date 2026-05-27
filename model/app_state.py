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
        self.totalTime =  "01:23:45"
        self.currentDate =  time.strftime("%Y-%m-%d")
        self.labels_for_jobs = ["Devops", "Stonks"]
        self.todaysTotalTime = "00:00:00"
        self.currentJob = "Devops"

        self.currentSession = "00:00:00"

        self.running_job = False
        self.running_pause = False
        self.session_job_seconds = 0
        self.session_pause_seconds = 0


        self.job_durations = {"Devops":"00:00:00", "Stonks":"00:00:00", "Other":"00:00:00"}


            

