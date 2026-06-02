class HomeController:
    def __init__(self, state, delete_service, time_service):
        self.state = state
        self.delete_service = delete_service
        self.time_service = time_service

    def undo_delete(self):
        job_time = self.delete_service.undo_deletion(self.state)
        #update total
        self.state.totalTime = self.time_service.add_times(self.state.totalTime, job_time)