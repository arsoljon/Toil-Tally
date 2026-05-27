from dataclasses import dataclass, field
import time

@dataclass
class AppState:
    currentDate: str = ""
    currentJob: str = ""
    job_selected: str = ""
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
    lengthOfSession: str = ""

    deleted_jobs: dict[str, str] = field(default_factory=dict)
    

    lengthOfPauseSession: str = ""
        
    style: str = ""
    size: int = 0
    #default is true if I do not want to save to the database. Do not save to db
    default: bool = True

    def setup(self):
        if self.default == True:
            self.totalTime =  "01:23:45"
            self.currentDate =  time.strftime("%Y-%m-%d")
            self.labels_for_jobs = ["Devops", "Stonks"]
            self.todaysTotalTime = "00:00:00"
            self.currentJob = "Devops"

            self.lengthOfPauseSession = "00:00:00"
            self.currentPauseTime = "00:00:00"
            self.startPauseTime = "00:00:00"
            self.lengthOfSession = "01:30:31"
            self.currentSession = "00:00:00"

            self.running_job = False
            self.running_pause = False
            self.session_job_seconds = 0
            self.session_pause_seconds = 0

            self.job_selected = ""
            self.style = "Arial"
            self.job_durations = {"Devops":"00:00:00", "Stonks":"00:00:00", "Other":"00:00:00"}
            self.deleted_jobs = {}

            self.size = int(16 * .8)

