import tkinter as tk
import time


class HomeFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.todaysTotalTime = "00:26:33"
        self.buttonLabels = ["Start", "Add"]
        #text
        self.label_currentDate = tk.Label(self, font=("Arial", 16))
        self.label_currentDate.pack(pady=20)
        self.label_totalTime = tk.Label(self, font=("Arial", 16))
        self.label_totalTime.pack(pady=20)
        self.label_todaysTotalTime = tk.Label(self, text= f"Todays Total: {self.todaysTotalTime}", font=("Arial", 16))
        self.label_todaysTotalTime.pack(pady=20)
        #buttons
        self.button1 = tk.Button(self, text=buttonLabels[0], command=self.on_click)
        self.button1.pack()
        self.button2 = tk.Button(self, text=buttonLabels[1], command=self.on_click)
        self.button2.pack()

    def on_click(self):
        buttonMessage = "Button clicked!"
        print(buttonMessage)

    def getButtons(self):
        return self.buttonLabels
    def getTodaysTotalTime(self):
        return self.todaysTotalTime

class ClockedInFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.lengthOfSession = "01:02:03"
        self.buttonLabels = ["End", "Pause"]
        #text
        self.label_currentDate = tk.Label(self, font=("Arial", 16))
        self.label_currentDate.pack(pady=20)
        self.label_totalTime = tk.Label(self, font=("Arial", 16))
        self.label_totalTime.pack(pady=20)
        self.label_lengthOfSession = tk.Label(self, text= f"Total: {self.lengthOfSession}", font=("Arial", 16))
        self.label_lengthOfSession.pack(pady=20)
        #buttons
        self.button_end = tk.Button(self, text=buttonLabels[0], command=self.on_click)
        self.button_end.pack()
        self.button_pause = tk.Button(self, text=buttonLabels[1], command=self.on_click)
        self.button_pause.pack()

    def on_click(self):
        buttonMessage = "Button clicked!"
        print(buttonMessage)

    def getButtons(self):
        return self.buttonLabels
    def getLengthOfSession(self):
        return self.lengthOfSession

class AddTimeFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.timeSelection= "00:00:00"
        self.buttonLabels = ["Add"]
        self.label_currentDate = tk.Label(self, font=("Arial", 16))
        self.label_currentDate.pack(pady=20)
        self.label_totalTime = tk.Label(self, font=("Arial", 16))
        self.label_totalTime.pack(pady=20)

    def getButtons(self):
        return self.buttonLabels
    def getTimeSelection(self):
        return self.timeSelection

class PauseFrame(tk.Frame):
    def __init__(self, parent, sessionLength):
        super().__init__(parent)
        self.lengthOfSession = sessionLength
        self.lengthOfPauseSession = "00:00:00"
        self.buttonLabels = ["End", "Continue"]
        #text
        self.label_currentDate = tk.Label(self, font=("Arial", 16))
        self.label_currentDate.pack(pady=20)
        self.label_totalTime = tk.Label(self, font=("Arial", 16))
        self.label_totalTime.pack(pady=20)
        self.label_lengthOfSession = tk.Label(self, text= f"Total: {self.lengthOfSession}", font=("Arial", 16))
        self.label_lengthOfSession.pack(pady=20)
        self.label_lengthOfSession = tk.Label(self, text= f"Pause for: {self.lengthOfPauseSession}", font=("Arial", 16))
        self.label_lengthOfSession.pack(pady=20)
        #buttons
        self.button1 = tk.Button(self, text=buttonLabels[0], command=self.on_click)
        self.button1.pack()
        self.button2 = tk.Button(self, text=buttonLabels[1], command=self.on_click)
        self.button2.pack()

    def on_click(self):
        buttonMessage = "Button clicked!"
        print(buttonMessage)


    def getButtons(self):
        return self.buttonLabels
    def getLengthOfSession(self):
        return self.lengthOfSession
    def getLengthOfPauseSession(self):
        return self.lengthOfPauseSession

class AppUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.currentDate = time.strftime("%Y-%m-%d")
        self.totalTime = "01:23:45"
        

        self.geometry("400x300+100+600")
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
       
    
        self.frames = {}
        self.frames[HomeFrame] = HomeFrame(container)
        self.frames[ClockedInFrame] = ClockedInFrame(container)
        session_length = self.frames[ClockedInFrame].getLengthOfSession()
        self.frames[PauseFrame] = PauseFrame(container, session_length)
        self.framesTitles = ["Default", "ClockedInScreen", "AddTimeScreen", "PauseScreen"]
        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(ClockedInFrame)


    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.label_currentDate.config(text=f"Date: {self.currentDate}")
        frame.label_totalTime.config(text=f"Total Time: {self.totalTime}")
        frame.tkraise()
        
        

windowTitles = ["Default", "ClockedInScreen", "AddTimeScreen", "PauseScreen"]
currentDate = time.strftime("%Y-%m-%d")
totalTime = "01:23:45"
todaysTotalTime = "00:26:33"
buttonLabels = ["Start", "Add"]

windowSize = "400x300+100+600"

prompt_currentDate = f"Date: {currentDate}"
prompt_totalTime = f"Total Time: {totalTime}"
prompt_todaysTotalTime = f"Accumulated Today: {todaysTotalTime}"

buttonLabel = "Click me"
'''
default = tk.Tk()
default.title(windowTitles[0])
default.geometry(windowSize)

label_currentDate = tk.Label(default, text=prompt_currentDate , font=("Arial", 16))
label_currentDate.pack(pady=20)
label_totalTime = tk.Label(default, text=prompt_totalTime , font=("Arial", 16))
label_totalTime.pack(pady=20)
label_todaysTotalTime = tk.Label(default, text=prompt_todaysTotalTime , font=("Arial", 16))
label_todaysTotalTime.pack(pady=20)

def on_click():
    ButtonMessage = "Button clicked!"
    print(ButtonMessage)

button1 = tk.Button(default, text=buttonLabels[0], command=on_click)
button1.pack()
button2 = tk.Button(default, text=buttonLabels[1], command=on_click)
button2.pack()
'''

if __name__ == "__main__":
    app = AppUI()
    app.mainloop()