import tkinter as tk
from services.time_services import TimeService

class AddTimeFrame(tk.Frame):
    def __init__(self, parent, controller, state):
        super().__init__(parent)
        self.controller = controller
        self.time_service = TimeService()

        #text
        self.style = controller.style
        self.size = controller.size

        self.grid(padx=1, pady=1)
        self.label_currentDate = tk.Label(self, text=f"Date: {state.currentDate}", font=(self.style, self.size))
        self.label_currentDate.grid(row=0, column=0, sticky="w")
        self.label_totalTime = tk.Label(self, text=f"Total Time: {state.totalTime}", font=(self.style, self.size))
        self.label_totalTime.grid(row=0, column=1, sticky="e")
        
        #input
        self.time_frame = tk.Frame(self)
        self.time_frame.grid(row=1, column=1, columnspan=2, pady=100, sticky="w")
        
        #buttons
        self.button1 = tk.Button(self, text=controller.addTime_buttons[0], command= lambda: self.add_time_on_click(controller, state))
        self.button1.grid(row=1, column=0)
        self.button2 = tk.Button(self, text=controller.addTime_buttons[1], command= lambda: self.cancel_on_click(controller, state))
        self.button2.grid(row=2, column=0)
        self.refresh(state)

    def add_time_on_click(self, controller, state):
        #add time
        if(state.currentJob == "Other"):
            if(len(self.entry.get()) <= 0 or
                self.entry.get().lower() in (
                    key.lower() for key in state.job_durations.keys()
                )
            ):
                return 
            else:
                self.time_service.add_new_job(state, self.entry.get())
        session = [int(self.hour.get()), int(self.minute.get()), 0]
        state.session_job_seconds = self.time_service.time_to_seconds(session)
        self.time_service.add_session_to_job(state)

        controller.show_frame(controller.addTime_pages[0], state)

    def cancel_on_click(self, controller, state):
        controller.show_frame(controller.addTime_pages[0], state)

    def refresh(self, state):
        for widget in self.time_frame.winfo_children():
            widget.destroy()
        if (state.currentJob == "Other"):
            #enter new job
            tk.Label(
                self.time_frame, 
                text="New Job:",
                font=(self.style, self.size)
            ).pack(side="left", padx=10)
            self.entry = tk.Entry(self.time_frame)
            self.entry.pack(side="left")
        else:
            tk.Label(
                self.time_frame, 
                text=state.currentJob,
                font=(self.style, self.size)
            ).pack(side="left", padx=10)

        tk.Label(
            self.time_frame,
            text="hh",
            font=(self.style, self.size)
        ).pack(side="left")
        self.hour = tk.Spinbox(
            self.time_frame,
            from_=0, 
            to=23, 
            width=3, 
            format="%02.0f"
        )
        self.hour.pack(side="left")
        tk.Label(
            self.time_frame, 
            text="mm", 
            font=(self.style, self.size)
        ).pack(side="left")
        self.minute = tk.Spinbox(
            self.time_frame, 
            from_=0, 
            to=59, 
            width=3, 
            format="%02.0f"
        )
        self.minute.pack(side="left")
        