class AddTimeService():
    def __init__(self):
        pass

    def parse_time(self, totalSession, currentTotal):
        #parse the time of session and total
        session_hh, session_mm, session_ss = map(int, totalSession.split(":"))
        total_hh, total_mm, total_ss = map(int, currentTotal.split(":"))
        updated_ss = session_ss + total_ss
        updated_mm = session_mm + total_mm
        updated_hh = session_hh + total_hh
        if(updated_ss > 59):
            remainder = updated_ss - 60
            updated_mm = updated_mm + 1
            updated_ss = remainder
        if(updated_mm > 59):
            remainder = updated_mm - 60
            updated_hh = updated_hh + 1
            updated_mm = remainder
        return f"{updated_hh:02}:{updated_mm:02}:{updated_ss:02}"