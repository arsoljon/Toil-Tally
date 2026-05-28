class StatusService():
    def reset_job_status(self, state):
        state.running_job = False
        state.running_pause = False 
        state.session_job_seconds = 0
        state.session_pause_seconds = 0
        state.session_initial = 0
        state.session_current = 0

    def is_running(self, state):
        if state.running_job: 
            state.session_job_seconds += 1
        elif state.running_pause:
            state.session_pause_seconds += 1
        else:
            return False
        return True

    def doing_job(self, state):
        state.running_job = True
        state.running_pause = False
        
    def taking_break(self, state):
        state.running_job = False
        state.running_pause = True 