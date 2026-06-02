from services.time_services import TimeService
from services.database.database_service import DatabaseService
import time

class StateService():
    def get_total_time(self, jobs):
        time_service = TimeService()
        total = 0
        for job, duration in jobs.items():
            seconds = time_service.time_to_seconds(time_service.parse_time(duration))
            total += seconds
        formatted_total = time_service.time_to_string(time_service.parse_seconds(total))
        return formatted_total
    
    def get_todays_total_time(self, currentDate):
        #add all sessions made from todays date
        db = DatabaseService()
        time_service = TimeService()
        seconds = db.get_total_sessions_by_date(currentDate)
        formatted_total = time_service.time_to_string(time_service.parse_seconds(seconds))
        return formatted_total
    
    def update_state(self, controller, state):
        db = DatabaseService()
        db.update_jobs(controller, state)
        
    def update_session_initial(self, state):
        state.session_initial = int(time.time())

    def update_session(self, state):
        #get the difference between session_initail and session_current
        #where both are time stamps, in seconds, of when they were made. 
        state.session_current = int(time.time())
        diff_seconds = abs(state.session_current - state.session_initial) - state.session_pause_seconds
        #update directly to the session_job_seconds
        state.session_job_seconds = diff_seconds

    def get_labels(self, items):
        labels = []
        for name, value in items.items():
            labels.append(name.replace("_", " "))
        return labels
    
    def get_all_weeks(self):
        db = DatabaseService()
        #get week_dates from weeks
        weeks = db.get_weeks()
        print("All weeks", weeks)
        #get all jobs and sort them via weeks_id
        all_jobs = db.get_all_jobs(weeks)
        print(all_jobs)
        #get job count from all jobs with the same week_id
        #get total hours from all jobs with the same week_id
        #avg
        #topjob
        return [{"week_date":"2026/05/26","job_count": 3,"total_hours": 45,"average": 12,"top_job": "Stonks"}, 
                {"week_date":"2026/05/23","job_count": 4,"total_hours": 55,"average": 22,"top_job": "Toil Tally"},
                {"week_date":"2026/05/22","job_count": 5,"total_hours": 65,"average": 32,"top_job": "Devops"}]