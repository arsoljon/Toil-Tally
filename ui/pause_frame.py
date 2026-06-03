import tkinter as tk

class PauseFrame(tk.Frame):
    def __init__(self, parent, ui_controller, pause_controller, state):
        super().__init__(parent)
        self.pause_controller = pause_controller
        self.buttonLabels = ui_controller.pause_buttons

        #text
        style = ui_controller.style
        size = ui_controller.size

        self.label_currentDate = tk.Label(self, text=f"Date: {state.currentDate}", font=(style, size))
        self.label_currentDate.grid(row=0, column=0, sticky="w")
        self.label_totalTime = tk.Label(self, text="", font=(style, size))
        self.label_totalTime.grid(row=0, column=1, sticky="ne")
        time = self.pause_controller.get_session_length()
        self.label_lengthOfSession = tk.Label(self, text= f"Total: {time}", font=(style, size))
        self.label_lengthOfSession.grid(row=2, column=0)
        paused_time = self.pause_controller.get_pause_length()
        self.label_lengthOfPausedSession = tk.Label(self, text= f"Pause for: {paused_time}", font=(style, size))
        self.label_lengthOfPausedSession.grid(row=3, column=0)
        #buttons
        self.button1 = tk.Button(self, text=self.buttonLabels[0], command= lambda: self.on_click_end(ui_controller, state))
        self.button1.grid(row=1, column=0)
        self.button2 = tk.Button(self, text=self.buttonLabels[1], command= lambda: self.on_click_clock_in(ui_controller, state))
        self.button2.grid(row=1, column=1)

    def on_click_end(self, ui_controller, state):
        #end, go to home frame
        #add the current session time to the current jobs time
        self.pause_controller.add_session_to_job()
        ui_controller.show_frame(ui_controller.pause_pages[0], state)

    def on_click_clock_in(self, ui_controller, state):
        #continue, go to clocked in frame
        ui_controller.show_frame(ui_controller.pause_pages[1], state)

    def update_display(self, state):
        paused_time = self.pause_controller.get_pause_length()
        session_time = self.pause_controller.get_session_length()
        self.label_lengthOfSession.config(text=f"{state.currentJob} : {session_time}")
        self.label_lengthOfPausedSession.config(text=f"Paused for: {paused_time}")
        self.label_totalTime.config(text=f"Time Spent on {state.currentJob}: {state.job_durations[state.currentJob]}")