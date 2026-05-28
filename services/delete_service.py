from services.time_services import TimeService

class DeleteService:
    def __init__(self):
        self.timeservice = TimeService()

    def delete_job(self, controller, state, job):
        if (job != "Other"):
            job_duration = state.job_durations[job]
            job_index = 0
            for i, label in enumerate(state.labels_for_jobs):
                if label == job:
                    job_index = i
            del state.job_durations[job]
            del state.labels_for_jobs[job_index]
            state.deleted_jobs[job] = job_duration
            #remove from total time: 
            totalDiff = self.timeservice.get_difference(state.totalTime, state.deleted_jobs[job])
            state.totalTime = totalDiff    
            todaysDiff = self.timeservice.get_difference(state.todaysTotalTime, state.deleted_jobs[job])
            state.todaysTotalTime = todaysDiff            
        else:
            print("Unable to delete")

    def undo_deletion(self, controller, state):
        if len(state.deleted_jobs) > 0:
            deleted = list(state.deleted_jobs.items())
            index = len(deleted) - 1
            job_key, job_time = deleted[index]
            del state.deleted_jobs[job_key]
            state.job_durations[job_key] = job_time
            state.labels_for_jobs.append(job_key)
            #update total
            newTotal = self.timeservice.add_times(state.totalTime, job_time)
            state.totalTime = newTotal

        else:
            print("Unable to Undo")