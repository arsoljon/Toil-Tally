import tkinter as tk
from controllers.app_controller import AppController
from ui.home_frame import HomeFrame 
from ui.add_time_frame import AddTimeFrame
from ui.pause_frame import PauseFrame
from ui.clock_in_time_frame import ClockedInFrame
from ui.weeks_frame import ViewWeeksFrame 
from ui.graph_frame import GraphFrame
from ui.notes_frame import NotesFrame
from model.app_state import AppState 
from services.status_service import StatusService


class AppUI(tk.Tk):
    def __init__(self):
        super().__init__()
        new_state = AppState()
        new_state.setup()
        self.app_controller = AppController(new_state)
        self.status_service = StatusService()
        
        self.home_pages = [ClockedInFrame, AddTimeFrame, HomeFrame, ViewWeeksFrame]
        self.clockedIn_pages = [HomeFrame, PauseFrame]
        self.pause_pages = [HomeFrame, ClockedInFrame]
        self.addTime_pages = [HomeFrame]
        self.viewWeeks_pages = [HomeFrame, GraphFrame]
        self.graph_pages = [ViewWeeksFrame, NotesFrame]
        self.notes_pages = [GraphFrame, ViewWeeksFrame, HomeFrame]
        self.home_buttons = ["Start", "Add", "Delete", "Undo", "Save & Exit", "View By Weeks"]        
        self.pause_buttons = ["End", "Continue"]
        self.addTime_buttons = ["Add", "Cancel"]
        self.clockedIn_buttons =  ["End", "Pause", "Update"]
        self.viewWeeks_buttons = ["Home"]
        self.graph_buttons = ["Back", "Notes"]
        self.notes_buttons = ["Back", "View Weeks" , "Save"]

        self.tick_job = None
        self.style = "Arial"
        self.size = int(16 * .8) 

        self.geometry("500x300+100+600")
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.frames[HomeFrame] = HomeFrame(
            container, self, self.app_controller.home_controller, new_state
        )
        self.frames[ClockedInFrame] = ClockedInFrame(
            container, self, self.app_controller.clock_in_controller, new_state
        )
        self.frames[PauseFrame] = PauseFrame(
            container, self, self.app_controller.pause_controller, new_state
        )
        self.frames[AddTimeFrame] = AddTimeFrame(
            container, self, self.app_controller.add_time_controller, new_state
        )
        self.frames[ViewWeeksFrame] = ViewWeeksFrame(
            container, self, self.app_controller.weeks_controller, new_state
        )
        self.frames[GraphFrame] = GraphFrame(
            container, self, self.app_controller.graph_controller, new_state
        )
        self.frames[NotesFrame] = NotesFrame(
            container, self, self.app_controller.notes_controller, new_state
        )

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")
        self.current_frame = HomeFrame
        self.show_frame(self.current_frame, new_state)

    def show_frame(self, frame_class, state):
        self.title(frame_class.__name__)
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
