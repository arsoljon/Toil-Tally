import tkinter as tk
import time
from ui.home_frame import HomeFrame 
from ui.add_time_frame import AddTimeFrame
from ui.pause_frame import PauseFrame
from ui.clock_in_time_frame import ClockedInFrame
from model.app_state import AppState

class AppUI(tk.Tk):
    def __init__(self):
        super().__init__()
        new_state = AppState()
        new_state.setup()
        
        new_state.home_pages = [ClockedInFrame, AddTimeFrame]
        new_state.ClockedIn_pages = [HomeFrame, PauseFrame]
        new_state.Pause_pages = [HomeFrame, ClockedInFrame]
        new_state.AddTime_pages = [HomeFrame]
        new_state.home_buttons = ["Start", "Add"]        
        new_state.Pause_buttons = ["End", "Continue"]
        new_state.AddTime_buttons = ["Add", "Cancel"]
        new_state.ClockedIn_buttons =  ["End", "Pause"]

        print(new_state.currentDate)
        self.state = {
            "currentDate" : time.strftime("%Y-%m-%d"),
            "totalTime" : "01:23:45",
            "todaysTotalTime" : "00:26:33",
            "Home buttons" : ["Start", "Add"],
            "Home pages" : [ClockedInFrame, AddTimeFrame],
            "labels_for_jobs" : ["Devops", "Stonks", "Other"],
            "ClockedIn pages" : [HomeFrame, PauseFrame],
            "currentJob" : "Devops",
            "lengthOfSession" : "01:30:31",
            "ClockedIn buttons": ["End", "Pause"],
            "AddTime pages" : [HomeFrame],
            "add timeSelection" : "00:00:00",
            "AddTime buttons" : ["Add", "Cancel"],
            "Pause pages" : [HomeFrame, ClockedInFrame],
            "lengthOfPauseSession" : "00:00:00",
            "Pause buttons" : ["End", "Continue"],
            "job_selected" : tk.StringVar(value="Other"),
            "job_durations" : {"Devops":"00:00:00", "Stonks":"00:00:00", "Other":"00:00:00"},
            "style" : "Arial",
            "size" : int(16 * .8),
        }   
        self.currentDate = time.strftime("%Y-%m-%d")
        self.totalTime = "01:23:45"
    
        self.geometry("500x300+100+600")
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.frames[HomeFrame] = HomeFrame(container, self)
        self.frames[ClockedInFrame] = ClockedInFrame(container, self)
        self.frames[PauseFrame] = PauseFrame(container, self)
        self.frames[AddTimeFrame] = AddTimeFrame(container, self)

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(HomeFrame)

    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        if hasattr(frame, "refresh"):
            frame.refresh()
        frame.tkraise()

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
