import tkinter as tk
from services.time_services import TimeService

class PauseFrame(tk.Frame):
    def __init__(self, parent, controller, state):
        super().__init__(parent)
        self.time_service = TimeService()
        self.buttonLabels = controller.pause_buttons

        #text
        style = controller.style
        size = controller.size

        self.label_currentDate = tk.Label(self, text=f"Date: {state.currentDate}", font=(style, size))
        self.label_currentDate.grid(row=0, column=0, sticky="w")
        self.label_totalTime = tk.Label(self, text="", font=(style, size))
        self.label_totalTime.grid(row=0, column=1, sticky="ne")
        
        self.label_lengthOfSession = tk.Label(self, text= f"Total: {state.lengthOfSession}", font=(style, size))
        self.label_lengthOfSession.grid(row=2, column=0)
        self.label_lengthOfPausedSession = tk.Label(self, text= f"Pause for: {state.lengthOfPauseSession}", font=(style, size))
        self.label_lengthOfPausedSession.grid(row=3, column=0)
        #buttons
        self.button1 = tk.Button(self, text=self.buttonLabels[0], command= lambda: self.on_click_end(controller, state))
        self.button1.grid(row=1, column=0)
        self.button2 = tk.Button(self, text=self.buttonLabels[1], command= lambda: self.on_click_clock_in(controller, state))
        self.button2.grid(row=1, column=1)

    def on_click_end(self, controller, state):
        #end, go to home frame
        #add the current session time to the current jobs time
        self.time_service.add_session_to_job(state)
        controller.show_frame(controller.pause_pages[0], state)

    def on_click_clock_in(self, controller, state):
        #continue, go to clocked in frame
        controller.show_frame(controller.pause_pages[1], state)

    def on_click(self, controller, buttonLabel, state):
        if(buttonLabel == self.buttonLabels[0]):
            #end, go to home frame
            #add the current session time to the current jobs time
            self.time_service.add_session_to_job(state)
            controller.show_frame(controller.pause_pages[0], state)
        else:
            #continue, go to clocked in frame
            controller.show_frame(controller.pause_pages[1], state)

    def update_display(self, state):
        seconds = state.session_pause_seconds
        hh, mm, ss = self.time_service.parse_seconds(seconds)
        time = self.time_service.parse_seconds(state.session_job_seconds)
        self.label_lengthOfSession.config(text=f"{state.currentJob} : {self.time_service.time_to_string(time)}")
        self.label_lengthOfPausedSession.config(text=f"Paused for: {self.time_service.time_to_string([hh, mm, ss])}")
        self.label_totalTime.config(text=f"Time Spent on {state.currentJob}: {state.job_durations[state.currentJob]}")