import tkinter as tk

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
