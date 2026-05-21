class TimeService():
    def reset_job_status(self, state):
        state.running_job = False
        state.running_pause = False 
        state.session_job_seconds = 0
        state.session_pause_seconds = 0

    def is_running(self, state):
        if state.running_job: 
            state.session_job_seconds += 1
        elif state.running_pause:
            state.session_pause_seconds += 1
        else:
            return False
        return True

    def doing_job(self, state):
        state.session_pause_seconds = 0
        state.running_job = True
        state.running_pause = False
        
    def taking_break(self, state):
        state.running_job = False
        state.running_pause = True 
        
    def parse_seconds(self, seconds):
        hh = seconds // 3600
        mm = (seconds % 3600) // 60
        ss = seconds % 60
        return hh, mm, ss
    
    def add_times(self, sessionTime, currentTime):
        session = self.parse_time(sessionTime)
        current = self.parse_time(currentTime)
        total = []
        for a, b in zip(session, current):
            total.append(a + b)
        updated_time = self.check_for_carry(total)
        return self.time_to_string(updated_time)
    
    def get_difference(self, start, end):
        #get the difference between start and end
        h1, m1, s1 = self.parse_time(start)
        h2, m2, s2 = self.parse_time(end)
        seconds1 = h1 * 3600 + m1 * 60 + s1
        seconds2 = h2 * 3600 + m2 * 60 + s2
        diff = abs(seconds1 - seconds2)
        
        hh = diff // 3600
        diff = diff - (hh * 3600)
        mm = diff // 60
        diff = diff - (mm * 60)
        ss = diff
        return self.time_to_string([hh, mm, ss])


    
    def parse_time(self, time):
        #at the moment the time format is a string, "10:02:33"
        hh, mm, ss = map(int, time.split(":"))
        return hh, mm, ss
    
    def check_for_carry(self, time):
        hh, mm, ss = time

        mm += ss // 60
        ss %= 60
        hh += mm // 60
        mm %= 60
        return [hh, mm, ss]
    
    def time_to_string(self, time):
        return f"{time[0]:02}:{time[1]:02}:{time[2]:02}"
    