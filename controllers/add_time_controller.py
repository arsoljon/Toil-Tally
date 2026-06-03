
class AddTimeController:
    def __init__(self, state, time_service, db):
        self.state = state
        self.db = db
        self.time_service = time_service

    def add_time_to_job(self, job_name, hour, minute):
        valid_job = self.time_service.add_new_job(self.state, job_name)
        if valid_job:
            time_entered = [hour, minute, 0]
            self.state.session_job_seconds = self.time_service.time_to_seconds(time_entered)
            self.time_service.add_session_to_job(self.state)
            self.db.insert_job(
                (self.state.currentJob, 
                self.state.job_durations[self.state.currentJob], 
                self.state.start_of_week,
                self.state.currentDate)
            )
            self.db.insert_session(self.state)
        return valid_job