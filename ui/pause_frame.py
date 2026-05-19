import tkinter as tk
from services.pause_services import PauseService

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
            #end, go to home frame
            #add the current session time to the current jobs time
            print(f"{self.buttonLabels[0]}!")
            controller.show_frame(self.pages[0])
        else:
            #continue, go to clocked in frame
            print(f"{self.buttonLabels[1]}!")
            controller.show_frame(self.pages[1])

    def getButtons(self):
        return self.buttonLabels
    def getLengthOfSession(self):
        return self.lengthOfSession
    def getLengthOfPauseSession(self):
        return self.lengthOfPauseSession
