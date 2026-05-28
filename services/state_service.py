from services.time_services import TimeService
from services.database.database_service import DatabaseService

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