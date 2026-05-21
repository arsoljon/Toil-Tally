import time
from add_time_services import AddTimeService
class TimeTracker():
    def __init__(self):
        self.addService = AddTimeService()

    def clock_in(self):
        return time.strftime("%H:%M:%S")
    
    def clock_out(self, start, end):
        time_spent = self.addService.get_difference(start, end) 
        return time_spent

    def update_time(self):
        return time.strftime("%H:%M:%S")
        
    def remove_time(self):
        return "00:00:00"