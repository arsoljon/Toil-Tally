from dataclasses import dataclass, field
import time


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
        self.currentDate =  time.strftime("%Y-%m-%d")
        self.totalTime =  "01:23:45"
        self.todaysTotalTime = "00:26:33"
        self.labels_for_jobs = ["Devops", "Stonks", "Other"]
        self.currentJob = "Devops"
        self.lengthOfSession = "01:30:31"
        self.available_jobs = ["Devops", "Stonks"]
        self.add_timeSelection = "00:00:00"
        self.lengthOfPauseSession = "00:00:00"

        self.job_selected = ""
        self.job_durations = {"Devops":"00:00:00", "Stonks":"00:00:00", "Other":"00:00:00"},
        self.style = "Arial"
        self.size = int(16 * .8)

    

