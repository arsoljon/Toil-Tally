class ClockInController:
    def __init__(self, state, time_service, state_service, db):
        self.db = db
        self.state = state
        self.time_service = time_service
        self.state_service = state_service

    def add_session_to_job(self):
        self.time_service.add_session_to_job(self.state)
        self.db.insert_job(
            (self.state.currentJob, 
            self.state.job_durations[self.state.currentJob], 
            self.state.start_of_week,
            self.state.currentDate)
        )
        self.db.insert_session(self.state)

    def get_session_length(self):
        length = self.time_service.time_to_string(
            self.time_service.parse_seconds(self.state.session_job_seconds)
        )
        return length
    
    def update_session(self):
        self.state_service.update_session(self.state)

    def update_session_display(self):
        hh,mm,ss = self.time_service.parse_seconds(self.state.session_job_seconds)
        return hh, mm, ss