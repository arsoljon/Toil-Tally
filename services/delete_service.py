class DeleteService:
    def delete_job(self, state, job):
        if (job != "Other"):
            print("Deleted job: ", job)
        else:
            print("Unable to delete")