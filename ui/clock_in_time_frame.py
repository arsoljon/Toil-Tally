import tkinter as tk
import time
from services.time_services import TimeService
from services.state_service import StateService

class ClockedInFrame(tk.Frame):
    def __init__(self, parent, controller, state):
        super().__init__(parent)
        state.running = True
        self.state_service = StateService()
        self.time_service = TimeService()
        self.controller = controller
        self.buttonLabels = controller.clockedIn_buttons
        #text
        style = controller.style
        size = controller.size
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        
        #frame setup
        self.labelFrame_header = tk.Frame(self)
        self.labelFrame_header.grid(row=0, column=0, padx=10, pady=5)
        self.buttonFrame_end_pause = tk.Frame(self)
        self.buttonFrame_end_pause.grid(row=1, column=0, sticky="w", padx=10)
        self.labelFrame_job_session = tk.Frame(self)
        self.labelFrame_job_session.grid(row=3, column=0, sticky="w", padx=10, pady=10)
        self.buttonFrame_update = tk.Frame(self)
        self.buttonFrame_update.grid(row=5, column=0, sticky="w", padx = 10)

        self.label_currentDate = tk.Label(self.labelFrame_header, text=f"Date: {state.currentDate}", font=(style, size))
        self.label_currentDate.grid(row=0, column=0, sticky="w")
        self.label_totalTime = tk.Label(self.labelFrame_header, text="", font=(style, size))
        self.label_totalTime.grid(row=0, column=1, sticky="ne", padx=100)
        
        self.label_currentJob = tk.Label(self.labelFrame_job_session, text= "", font=(style, size))
        self.label_currentJob.grid(row=0, column=0, sticky = "w")
        time = self.time_service.time_to_string(self.time_service.parse_seconds(state.session_job_seconds))
        self.label_lengthOfSession = tk.Label(self.labelFrame_job_session, text= f"Total: {time}", font=(style, size))
        self.label_lengthOfSession.grid(row=1, column=0, sticky = "w")

        #buttons
        self.button1 = tk.Button(self.buttonFrame_end_pause, text=self.buttonLabels[0], command= lambda: self.on_click_end(controller, state))
        self.button1.grid(row=0, column=0, sticky="w", padx = 10)
        self.button2 = tk.Button(self.buttonFrame_end_pause, text=self.buttonLabels[1], command= lambda: self.on_click_pause(controller, state))
        self.button2.grid(row=0, column=1, sticky="e", padx = 200)
        self.button3 = tk.Button(self.buttonFrame_update,text=self.buttonLabels[2], command= lambda: self.on_click_update(controller, state))
        self.button3.grid(row=0, column=0)
    
    def on_click_update(self, controller, state):
        self.state_service.update_session(state)

    def on_click_end(self, controller, state):
        #end
        self.time_service.add_session_to_job(controller, state)
        controller.show_frame(controller.clockedIn_pages[0], state)

    def on_click_pause(self, controller, state):
        #pause
        controller.show_frame(controller.clockedIn_pages[1], state)

    def refresh(self, state):
        currentJob = state.currentJob
        self.totalTime = state.job_durations[currentJob]

        self.label_totalTime.config(text=f"Time Spent on {state.currentJob}: {state.job_durations[state.currentJob]}")
        self.label_currentJob.config(text=state.currentJob)

    def update_display(self, state):
        seconds = state.session_job_seconds
        hh, mm, ss = self.time_service.parse_seconds(seconds)
        self.label_lengthOfSession.config(text=f"{hh:02}:{mm:02}:{ss:02}")
