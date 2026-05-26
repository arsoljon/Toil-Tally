from dataclasses import dataclass, field
import time

@dataclass
class AppState:


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

