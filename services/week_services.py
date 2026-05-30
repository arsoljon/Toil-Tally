from datetime import timedelta, datetime, time

class WeekService():
    def get_start_of_week(self):
        #using datetime lib, days are represented: 
        # 0-6 => Monday-Sunday 
        seconds_per_day = timedelta(days=1).total_seconds()
        today = datetime.now()
        seconds_today = today.timestamp()
        if today.weekday() < 6:
            diff = seconds_per_day * (today.weekday() + 1)
            seconds_today = seconds_today - diff
        date = datetime.fromtimestamp(seconds_today).date()
        print("Start of the week: ", date)

    def get_job_count(self, state):
        return len(state.job_durations)

    def get_total_hours(self, state):
        sum = 0
        for job in state.job_durations:
            name, hours = list(job)
            sum += hours
        return sum        

    def get_avg_per_day(self, state):
        sum = self.get_total_hours(state)
        days = 7
        return int(sum/days)

    def get_top_job(self, state):
        top_job = ""
        top_hours = 0
        for job in state.job_durations:
            name, hours = list(job)
            if hours > top_hours:
                top_hours = hours
                top_job = name
        return top_job