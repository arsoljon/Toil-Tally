import tkinter as tk

class AddTimeFrame(tk.Frame):
    def __init__(self, parent, controller, state):
        super().__init__(parent)
        self.controller = controller
        self.currentDate = state.currentDate
        self.totalTime = state.totalTime
        self.timeSelection = state.add_timeSelection
        self.buttonLabels = controller.addTime_buttons
        self.selected = tk.StringVar(value=state.job_selected)
        self.pages = controller.addTime_pages
        self.jobDurations = state.job_durations
        #text
        self.style = state.style
        self.size = state.size

        self.grid(padx=1, pady=1)
        self.label_currentDate = tk.Label(self, text=f"Date: {self.currentDate}", font=(self.style, self.size))
        self.label_currentDate.grid(row=0, column=0, sticky="w")
        self.label_totalTime = tk.Label(self, text=f"Total Time: {self.totalTime}", font=(self.style, self.size))
        self.label_totalTime.grid(row=0, column=1, sticky="e")
        
        #input
        self.time_frame = tk.Frame(self)
        self.time_frame.grid(row=1, column=1, columnspan=2, pady=100, sticky="w")
        #entry
        '''
        if(self.selected.get() == "Other"):
            tk.Label(time_frame, text="New Job:", font=(style, size)).pack(side="left", padx=10)
            self.entry = tk.Entry(time_frame)
            self.entry.pack(side="left", padx=0)
        else:
            tk.Label(time_frame, text=self.selected.get(), font=(style, size)).pack(side="left", padx=10)
        tk.Label(time_frame, text="hh", font=(style, size)).pack(side="left")
        self.hour = tk.Spinbox(time_frame, from_=0, to=23, width=3, format="%02.0f")
        self.hour.pack(side="left")
        tk.Label(time_frame, text="mm", font=(style, size)).pack(side="left")
        self.minute = tk.Spinbox(time_frame, from_=0, to=59, width=3, format="%02.0f")
        self.minute.pack(side="left")
        '''
    
        #buttons
        self.button1 = tk.Button(self, text=self.buttonLabels[0], command= lambda: self.on_click(controller, self.buttonLabels[0], state))
        self.button1.grid(row=1, column=0)
        self.button2 = tk.Button(self, text=self.buttonLabels[1], command= lambda: self.on_click(controller, self.buttonLabels[1], state))
        self.button2.grid(row=2, column=0)
        self.refresh(state)

    def on_click(self, controller, buttonLabel, state):
        if(buttonLabel == self.buttonLabels[0]):
            #add time
            print(f"{self.buttonLabels[0]}!")
            name_of_job = self.selected.get()
            
            previous_total = ""
            if (self.selected.get() == "Other"):
                #add new job
                if(len(self.entry.get()) > 0):
                    name_of_job = self.entry.get()
                    self.controller.state["labels_for_jobs"].append(name_of_job)
                    
            if(name_of_job not in self.jobDurations):
                previous_total = "00:00:00"
            else:
                previous_total = self.jobDurations[name_of_job]
            new_hh = int(self.hour.get())
            new_mm = int(self.minute.get())            
            total_entry = f"{new_hh:2}:{new_mm:2}:00"
            updated_total = controller.parse_time(total_entry, previous_total )
            self.jobDurations[name_of_job] = updated_total
            self.controller.state["job_durations"] = self.jobDurations
            controller.show_frame(self.pages[0], state)
        else:
            #cancel
            print(f"{self.buttonLabels[1]}!")
            controller.show_frame(self.pages[0], state)

    def refresh(self, state):
        for widget in self.time_frame.winfo_children():
            widget.destroy()
        if (self.selected.get() == "Other"):
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
                text=self.selected.get(),
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
        
    
    def getButtons(self):
        return self.buttonLabels
    def getTimeSelection(self):
        return self.timeSelection