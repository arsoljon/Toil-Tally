class HomeController:
    def __init__(self, state, delete_service, time_service, state_service, db):
        self.state = state
        self.state_service = state_service
        self.delete_service = delete_service
        self.time_service = time_service
        self.db = db

    def undo_delete(self):
        job_time = self.delete_service.undo_deletion(self.state)
        #update total
        self.state.totalTime = self.time_service.add_times(self.state.totalTime, job_time)
    
    def delete_job(self, job):
        check_deleted = self.delete_service.delete_job(self.state, job)
        #remove from total time: 
        if check_deleted == True:
            self.state.totalTime = self.time_service.get_difference(self.state.totalTime, self.state.deleted_jobs[job]) 
            self.state.todaysTotalTime = self.time_service.get_difference(self.state.todaysTotalTime, self.state.deleted_jobs[job])

    def update_state(self):
        self.db.update_jobs(self.state)

    def update_session_initial(self):
        self.state_service.update_session_initial(self.state)