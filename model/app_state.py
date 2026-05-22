from dataclasses import dataclass, field
import time

@dataclass
class AppState:
    currentDate: str = ""
    todaysTotalTime: str = ""
    totalTime: str = ""
    currentJob: str = ""
    lengthOfSession: str = ""
    labels_for_jobs: list[str] = field(default_factory=list)
    job_durations: dict[str, str] = field(default_factory=dict)
    currentPauseTime: str = ""
    startPauseTime: str = ""
    currentSession: str = ""
    startTime: str = ""
    elapsed_seconds: int = 0
    running_job: bool = False
    running_pause: bool = False
    session_job_seconds: int= 0
    session_pause_seconds: int = 0

    
    add_timeSelection: str = ""
    lengthOfPauseSession: str = ""
    job_selected: str = ""
    
    home_pages: list[str] = field(default_factory=list)
    pause_pages: list[str] = field(default_factory=list)
    addTime_pages: list[str] = field(default_factory=list)
    clockedIn_pages: list[str] = field(default_factory=list)
    home_buttons: list[str] = field(default_factory=list)
    pause_buttons: list[str] = field(default_factory=list)
    addTime_buttons: list[str] = field(default_factory=list)
    clockedIn_buttons: list[str] = field(default_factory=list)
    
    style: str = ""
    size: int = 0
    #default is true if I do not want to save to the database. Do not save to db
    default: bool = True

    def setup(self):
        if self.default == True:
            self.totalTime =  "01:23:45"
            self.currentDate =  time.strftime("%Y-%m-%d")
            self.labels_for_jobs = ["Devops", "Stonks", "Other"]
            self.todaysTotalTime = "00:00:00"
            self.currentJob = "Devops"
            self.add_timeSelection = "00:00:00"
            self.available_jobs = ["Devops", "Stonks"]
            self.lengthOfPauseSession = "00:00:00"
            self.currentPauseTime = "00:00:00"
            self.startPauseTime = "00:00:00"
            self.lengthOfSession = "01:30:31"
            self.currentSession = "00:00:00"
            self.startTime = "00:00:00"
            self.running_job = False
            self.running_pause = False
            self.session_job_seconds = 0
            self.session_pause_seconds = 0

            self.job_selected = "Other"
            self.style = "Arial"
            self.job_durations = {"Devops":"00:00:00", "Stonks":"00:00:00", "Other":"00:00:00"}

            self.size = int(16 * .8)

'''

class AppState():
    def __init__(self):
        self.currentDate =  ""
        self.todaysTotalTime =  ""
        self.totalTime =  ""
        self.currentJob = ""
        self.lengthOfSession = ""
        self.labels_for_jobs = []
        self.job_durations = {}
        
        self.add_timeSelection = ""
        self.lengthOfPauseSession = ""
        self.job_selected = ""
        
        self.home_pages = []
        self.Pause_pages = []
        self.AddTime_pages = []
        self.ClockedIn_pages = []
        self.home_buttons = []
        self.Pause_buttons = []
        self.AddTime_buttons = []
        self.ClockedIn_buttons =  []
        
        self.style = ""
        self.size = 0
        #default is true if I do not want to save to the database. Do not save to db
        self.default = True

    def default_setup(self):
        self.totalTime =  "01:23:45"
        self.currentDate =  time.strftime("%Y-%m-%d")
        self.labels_for_jobs = ["Devops", "Stonks", "Other"]
        self.todaysTotalTime = "00:26:33"
        self.lengthOfSession = "01:30:31"
        self.currentJob = "Devops"
        self.add_timeSelection = "00:00:00"
        self.available_jobs = ["Devops", "Stonks"]
        self.lengthOfPauseSession = "00:00:00"

        self.job_selected = ""
        self.style = "Arial"
        self.job_durations = {"Devops":"00:00:00", "Stonks":"00:00:00", "Other":"00:00:00"},

        self.size = int(16 * .8)
    
'''
