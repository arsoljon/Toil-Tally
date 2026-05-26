class DeleteService:
    def delete_job(self, state, job):
        if (job != "Other"):
            #find the job listed in the jobDurations and labels_for_jobs
            #add the jobs name and time to jobs_deleted list
            #remove the amount of time of job from the totalTime
            job_duration = state.job_durations[job]
            job_index = 0
            for i, label in enumerate(state.labels_for_jobs):
                if label == job:
                    job_index = i
            del state.job_durations[job]
            del state.labels_for_jobs[job_index]
            state.deleted_jobs[job] = job_duration
            print("jobs deleted: ", state.deleted_jobs)       
        else:
            print("Unable to delete")