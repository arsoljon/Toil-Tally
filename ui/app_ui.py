import tkinter as tk
from ui.home_frame import HomeFrame 
from ui.add_time_frame import AddTimeFrame
from ui.pause_frame import PauseFrame
from ui.clock_in_time_frame import ClockedInFrame
from model.app_state import AppState 
from services.status_service import StatusService

class AppUI(tk.Tk):
    def __init__(self):
        super().__init__()
        new_state = AppState()
        new_state.setup()
        self.status_service = StatusService()
        
        self.home_pages = [ClockedInFrame, AddTimeFrame]
        self.clockedIn_pages = [HomeFrame, PauseFrame]
        self.pause_pages = [HomeFrame, ClockedInFrame]
        self.addTime_pages = [HomeFrame]
        self.home_buttons = ["Start", "Add"]        
        self.pause_buttons = ["End", "Continue"]
        self.addTime_buttons = ["Add", "Cancel"]
        self.clockedIn_buttons =  ["End", "Pause"]

        self.start_time = "00:00:00"
        self.current_time = "00:00:00"
        self.tick_job = None

        self.geometry("500x300+100+600")
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.frames[HomeFrame] = HomeFrame(container, self, new_state)
        self.frames[ClockedInFrame] = ClockedInFrame(container, self, new_state)
        self.frames[PauseFrame] = PauseFrame(container, self, new_state)
        self.frames[AddTimeFrame] = AddTimeFrame(container, self, new_state)

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")
        self.current_frame = HomeFrame
        self.show_frame(self.current_frame, new_state)

    def show_frame(self, frame_class, state):
        self.current_frame = self.frames[frame_class]
        frame = self.frames[frame_class]
        if hasattr(frame, "refresh"):
            frame.refresh(state)
        frame.tkraise()

        ticking_frames = [ClockedInFrame, PauseFrame]
        if frame_class in ticking_frames:
            if self.tick_job is not None:
                self.after_cancel(self.tick_job)
                self.tick_job = None
            if frame_class == ClockedInFrame:
                self.status_service.doing_job(state)
            else:
                self.status_service.taking_break(state)
            self.tick(state)          
        else:
            self.status_service.reset_job_status(state)
            if self.tick_job is not None:
                self.after_cancel(self.tick_job)
                self.tick_job = None

    def tick(self, state):
        if not self.status_service.is_running(state):
            return 
        self.current_frame.update_display(state)
        self.tick_job = self.after(1000,self.tick, state)
