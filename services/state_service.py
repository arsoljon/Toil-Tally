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
        diff_seconds = abs(state.session_current - state.session_initial)
        #update directly to the session_job_seconds
        state.session_job_seconds = diff_seconds

