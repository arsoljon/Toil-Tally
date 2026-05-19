import tkinter as tk

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
