from datetime import timedelta, datetime, time
from services.time_services import TimeService

class WeekService():
    def __init__(self):
        self.time_service = TimeService()

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
        return date

    def get_job_count(self, jobs):
        return len(jobs)

    def get_total_hours(self, jobs):
        sum = self.get_total_seconds(jobs)
        hh, mm, ss = self.time_service.parse_seconds(sum)
        return self.time_service.time_to_string((hh,mm,ss))

    def get_total_seconds(self, jobs):
        sum = 0
        for hours_string in jobs.values():
            seconds = self.time_service.time_to_seconds(self.time_service.parse_time(hours_string))
            sum += seconds
        return sum

    def get_avg_per_day(self, jobs):
        sum = self.get_total_seconds(jobs)
        days = 7
        avg = int(sum/days)
        hh, mm, ss = self.time_service.parse_seconds(avg)
        return self.time_service.time_to_string((hh,mm,ss))

    def get_top_job(self, jobs):
        top_job = ""
        top_hours = 0
        for name, hours_string in jobs.items():
            hours = self.time_service.time_to_seconds(self.time_service.parse_time(hours_string))
            if hours > top_hours:
                top_hours = hours
                top_job = name
        return top_job
    
    def get_bar_info(self, state):
        jobs = []
        hours = []
        for name, duration in state.job_durations.items():
            jobs.append(name)
            formatted_duration = self.time_service.parse_time(duration)
            hours.append(formatted_duration[0])
        return jobs, hours