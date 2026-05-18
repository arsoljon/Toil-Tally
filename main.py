import tkinter as tk
from tkinter import font
import time


class HomeFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.currentDate = controller.state["currentDate"]
        self.totalTime = controller.state["totalTime"]
        self.todaysTotalTime = controller.state["todaysTotalTime"]
        self.buttonLabels = controller.state["Home buttons"]
        self.pages = controller.state["Home pages"]
        style = controller.state["style"]
        size = controller.state["size"]
        labels_jobs = controller.state["labels_for_jobs"]
        self.selected = controller.state["job_selected"]

        #text
        self.label_currentDate = tk.Label(self, text=f"Date: {self.currentDate}", font=(style, size))
        self.label_currentDate.grid(row=0, column=0, sticky="w")
        self.label_totalTime = tk.Label(self, text=f"Total Time {self.totalTime}", font=(style, size))
        self.label_totalTime.grid(row=0, column=1, sticky="e")
        self.label_todaysTotalTime = tk.Label(self, text= f"Todays Total: {self.todaysTotalTime}", font=(style, size))
        self.label_todaysTotalTime.grid(row=2, column=0, sticky="w")
        #buttons
        self.button1 = tk.Button(self, text=self.buttonLabels[0], command=lambda: self.on_click(controller, self.buttonLabels[0]))
        self.button1.grid(row=1, column=0, sticky="w")
        self.button2 = tk.Button(self, text=self.buttonLabels[1], command=lambda: self.on_click(controller, self.buttonLabels[1]))
        self.button2.grid(row=1, column=1, sticky="e")
        
        self.refresh()

    def on_click(self, controller, buttonLabel):
        if(buttonLabel == self.buttonLabels[0]):
            #clockIn
            print(f"{self.buttonLabels[0]} : {self.selected.get()}!")
            controller.state["currentJob"] = f"{self.selected.get()}"
            controller.show_frame(self.pages[0])
        else:
            #manually add to job
            controller.state["job_selected"] = self.selected
            print(f"{self.buttonLabels[1]} : selected {self.selected.get()}, !")
            controller.show_frame(self.pages[1])
    
    def refresh(self):
        #radiobuttons
        labels_jobs = self.controller.state["labels_for_jobs"]
        for i, job in enumerate(labels_jobs):
            rb = tk.Radiobutton(
                self,
                text=job,
                variable=self.selected,
                value=job
            )
            rb.grid(row=i+1, column= 1)
        print(self.controller.state["job_durations"])
        
    def getButtons(self):
        return self.buttonLabels
    def getTodaysTotalTime(self):
        return self.todaysTotalTime

class ClockedInFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.currentDate = controller.state["currentDate"]
        self.controller = controller
        #self.currentJob = controller.state["currentJob"]
        self.lengthOfSession = controller.state["lengthOfSession"]
        self.buttonLabels = controller.state["ClockedIn buttons"]
        self.pages = controller.state["ClockedIn pages"]
        #text
        style = controller.state["style"]
        size = controller.state["size"]
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        
        
        self.label_currentDate = tk.Label(self, text=f"Date: {self.currentDate}", font=(style, size))
        self.label_currentDate.grid(row=0, column=0, sticky="w")
        
        #self.label_currentJob = tk.Label(self, text= f"{self.currentJob}", font=(style, size))
        self.label_currentJob = tk.Label(self, text= "", font=(style, size))
        self.label_currentJob.grid(row=2, column=0, sticky = "w")
        self.label_lengthOfSession = tk.Label(self, text= f"Total: {self.lengthOfSession}", font=(style, size))
        self.label_lengthOfSession.grid(row=3, column=0, sticky = "w")
        #buttons
        self.button1 = tk.Button(self, text=self.buttonLabels[0], command= lambda: self.on_click(controller, self.buttonLabels[0]))
        self.button1.grid(row=1, column=0)
        self.button2 = tk.Button(self, text=self.buttonLabels[1], command= lambda: self.on_click(controller, self.buttonLabels[1]))
        self.button2.grid(row=1, column=1)
    
    def on_click(self, controller, buttonLabel):
        if(buttonLabel == self.buttonLabels[0]):
            #end
            totalSession = self.lengthOfSession
            jobDurations = self.controller.state["job_durations"]
            currentJob = self.controller.state["currentJob"]
            currentTotal = jobDurations[currentJob]

            #parse the time of session and total
            updated_total = controller.parse_time(totalSession, currentTotal)
            jobDurations[currentJob] = updated_total
            self.controller.state["job_durations"] = jobDurations
            print(f"{self.buttonLabels[0]}!")
            controller.show_frame(self.pages[0])
        else:
            #pause
            print(f"{self.buttonLabels[1]}!")
            controller.show_frame(self.pages[1])

    def refresh(self):
        style = self.controller.state["style"]
        size = self.controller.state["size"]
        currentJob = self.controller.state["currentJob"]
        self.totalTime = self.controller.state["job_durations"][currentJob]
        self.label_totalTime = tk.Label(self, text=f"Total Time: {self.totalTime}", font=(style, size))
        self.label_totalTime.grid(row=0, column=1, sticky="ne")
        
        self.label_currentJob.config(text=self.controller.state["currentJob"])

    def getButtons(self):
        return self.buttonLabels
    def getLengthOfSession(self):
        return self.lengthOfSession

class AddTimeFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.currentDate = controller.state["currentDate"]
        self.totalTime = controller.state["totalTime"]
        self.jobs = controller.state["available jobs"]
        self.timeSelection = controller.state["add timeSelection"]
        self.buttonLabels = controller.state["AddTime buttons"]
        self.selected = controller.state["job_selected"]
        self.pages = controller.state["AddTime pages"]
        self.jobDurations = controller.state["job_durations"]
        #text
        self.style = controller.state["style"]
        self.size = controller.state["size"]

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
        self.button1 = tk.Button(self, text=self.buttonLabels[0], command= lambda: self.on_click(controller, self.buttonLabels[0]))
        self.button1.grid(row=1, column=0)
        self.button2 = tk.Button(self, text=self.buttonLabels[1], command= lambda: self.on_click(controller, self.buttonLabels[1]))
        self.button2.grid(row=2, column=0)
        self.refresh()

    def on_click(self, controller, buttonLabel):
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
            controller.show_frame(self.pages[0])
        else:
            #cancel
            print(f"{self.buttonLabels[1]}!")
            controller.show_frame(self.pages[0])

    def refresh(self):
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

class PauseFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.currentDate = controller.state["currentDate"]
        self.totalTime = controller.state["totalTime"]
        self.lengthOfSession = controller.state["lengthOfSession"]
        self.lengthOfPauseSession = controller.state["lengthOfPauseSession"]
        self.buttonLabels = controller.state["Pause buttons"]
        self.pages = controller.state["Pause pages"]
        #text preprocessing
        #text
        style = controller.state["style"]
        size = controller.state["size"]

        self.label_currentDate = tk.Label(self, text=f"Date: {self.currentDate}", font=(style, size))
        self.label_currentDate.grid(row=0, column=0, sticky="w")
        self.label_totalTime = tk.Label(self, text=f"Total Time: {self.totalTime}", font=(style, size))
        self.label_totalTime.grid(row=0, column=1, sticky="ne")
        
        self.label_lengthOfSession = tk.Label(self, text= f"Total: {self.lengthOfSession}", font=(style, size))
        self.label_lengthOfSession.grid(row=2, column=0)
        self.label_lengthOfPausedSession = tk.Label(self, text= f"Pause for: {self.lengthOfPauseSession}", font=(style, size))
        self.label_lengthOfPausedSession.grid(row=3, column=0)
        #buttons
        self.button1 = tk.Button(self, text=self.buttonLabels[0], command= lambda: self.on_click(controller, self.buttonLabels[0]))
        self.button1.grid(row=1, column=0)
        self.button2 = tk.Button(self, text=self.buttonLabels[1], command= lambda: self.on_click(controller, self.buttonLabels[1]))
        self.button2.grid(row=1, column=1)

    def on_click(self, controller, buttonLabel):
        if(buttonLabel == self.buttonLabels[0]):
            print(f"{self.buttonLabels[0]}!")
            controller.show_frame(self.pages[0])
        else:
            print(f"{self.buttonLabels[1]}!")
            controller.show_frame(self.pages[1])

    def getButtons(self):
        return self.buttonLabels
    def getLengthOfSession(self):
        return self.lengthOfSession
    def getLengthOfPauseSession(self):
        return self.lengthOfPauseSession

class AppUI(tk.Tk):
    def __init__(self):
        super().__init__()

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
            "available jobs" : ["Devops", "Stonks"],
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

        
        
if __name__ == "__main__":
    app = AppUI()
    app.mainloop()