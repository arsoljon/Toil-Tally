class DeleteService:
    def delete_job(self, state, job):
        if (job != "Other"):
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

    def undo_deletion(self, state):
        if len(state.deleted_jobs) > 0:
            deleted = list(state.deleted_jobs.items())
            index = len(deleted) - 1
            job_key, job_time = deleted[index]
            del state.deleted_jobs[job_key]
            state.job_durations[job_key] = job_time
            state.labels_for_jobs.append(job_key)
        else:
            print("Unable to Undo")