import tkinter as tk
from tkinter import font
import time


class HomeFrame(tk.Frame):
    def __init__(self, parent, totalTime, currentDate):
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
    def __init__(self, parent, totalTime, currentDate):
        super().__init__(parent)
        self.lengthOfSession = "01:02:03"
        self.buttonLabels = ["End", "Pause"]
 #text
        style = "Arial"
        size_offset = .8
        size = int(16 * size_offset)
        my_text = font.Font(family=style, size=size)
        pixel_width = my_text.measure(currentDate)
        index = 0
        
        self.label_currentDate = tk.Label(self, text=f"Date: {currentDate}", font=(style, size))
        self.label_currentDate.grid(row=0, column=0, sticky="w")
        self.label_totalTime = tk.Label(self, text=f"Total Time: {totalTime}", font=(style, size))
        self.label_totalTime.grid(row=0, column=1, sticky="ne")

        self.label_lengthOfSession = tk.Label(self, text= f"Total: {self.lengthOfSession}", font=("Arial", 16))
        self.label_lengthOfSession.grid(row=2, column=0)
        #buttons
        self.button1 = tk.Button(self, text=self.buttonLabels[0], command=self.on_click)
        self.button1.grid(row=1, column=0)
        self.button2 = tk.Button(self, text=self.buttonLabels[1], command=self.on_click)
        self.button2.grid(row=1, column=1)

    def on_click(self):
        buttonMessage = "Button clicked!"
        print(buttonMessage)

    def getButtons(self):
        return self.buttonLabels
    def getLengthOfSession(self):
        return self.lengthOfSession

class AddTimeFrame(tk.Frame):
    def __init__(self, parent, totalTime, currentDate):
        super().__init__(parent)
        self.timeSelection= "00:00:00"
        self.buttonLabels = ["Add", "Cancel"]
       #text
        style = "Arial"
        size_offset = .8
        size = int(16 * size_offset)
        my_text = font.Font(family=style, size=size)
        pixel_width = my_text.measure(currentDate)
        index = 0
        
        self.label_currentDate = tk.Label(self, text=f"Date: {currentDate}", font=(style, size))
        self.label_currentDate.grid(row=0, column=0, sticky="w")
        self.label_totalTime = tk.Label(self, text=f"Total Time: {totalTime}", font=(style, size))
        self.label_totalTime.grid(row=0, column=1, sticky="e")
        #input
        self.label_hh = tk.Label(self, text="hh", font=(style, size))
        self.label_mm = tk.Label(self, text="mm", font=(style, size))
        self.label_hh.grid(row=1, column=1, sticky="e")
        self.label_mm.grid(row=1, column=3)
        hour = tk.Spinbox(self, from_=0, to=23, width=3, format="%02.0f")
        hour.grid(row=1, column=2)
        minute = tk.Spinbox(self, from_=0, to=59, width=3, format="%02.0f")
        minute.grid(row=1, column=4)
        #buttons
        self.button1 = tk.Button(self, text=self.buttonLabels[0], command=self.on_click)
        self.button1.grid(row=1, column=0)
        self.button2 = tk.Button(self, text=self.buttonLabels[1], command=self.on_click)
        self.button2.grid(row=2, column=0)

    def on_click(self):
        buttonMessage = "Button clicked!"
        print(buttonMessage)

    def getButtons(self):
        return self.buttonLabels
    def getTimeSelection(self):
        return self.timeSelection

class PauseFrame(tk.Frame):
    def __init__(self, parent, sessionLength, totalTime, currentDate):
        super().__init__(parent)
        self.lengthOfSession = sessionLength
        self.lengthOfPauseSession = "00:00:00"
        self.buttonLabels = ["End", "Continue"]
        #text preprocessing
        root = self.winfo_toplevel()
        root.update_idletasks()
        geometry_size, position= root.geometry().split("+", 1)
        width, height = map(int, geometry_size.split("x"))
        spacing = 5
        row_offset =  height/5 
        column_width_1 = int(width/2)
        column_offset_2 = width/5
        column_offset_3 = width/3


        print(f"width : {width}")
        #text
        style = "Arial"
        size_offset = .8
        size = int(16 * size_offset)
        my_text = font.Font(family=style, size=size)
        pixel_width = my_text.measure(currentDate)
        index = 0

        self.label_currentDate = tk.Label(self, text=f"Date: {currentDate}", font=(style, size))
        self.label_currentDate.grid(row=0, column=0, sticky="w")
        #self.label_currentDate.place(x= (0*row_offset) + (0*column_width_1) + spacing, y= (0*row_offset) + (0*column_width_1) +spacing)
        self.label_totalTime = tk.Label(self, text=f"Total Time: {totalTime}", font=(style, size))
        self.label_totalTime.grid(row=0, column=1, sticky="ne")
        #self.label_totalTime.place(x= 100 + spacing, y= (1*row_offset) + (0*column_width_1) +spacing)
        print(my_text.measure(totalTime))

        self.label_lengthOfSession = tk.Label(self, text= f"Total: {self.lengthOfSession}", font=(style, size))
        self.label_lengthOfSession.grid(row=2, column=0)
        self.label_lengthOfPausedSession = tk.Label(self, text= f"Pause for: {self.lengthOfPauseSession}", font=(style, size))
        self.label_lengthOfPausedSession.grid(row=3, column=0)
        #buttons
        self.button1 = tk.Button(self, text=self.buttonLabels[0], command=self.on_click)
        self.button1.grid(row=1, column=0)
        self.button2 = tk.Button(self, text=self.buttonLabels[1], command=self.on_click)
        self.button2.grid(row=1, column=1)
 
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
    
        self.geometry("500x300+100+600")
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}
        self.frames[HomeFrame] = HomeFrame(container, self.totalTime, self.currentDate)
        self.frames[ClockedInFrame] = ClockedInFrame(container, self.totalTime, self.currentDate)
        session_length = self.frames[ClockedInFrame].getLengthOfSession()
        self.frames[PauseFrame] = PauseFrame(container, session_length, self.totalTime, self.currentDate)
        self.frames[AddTimeFrame] = AddTimeFrame(container, self.totalTime, self.currentDate)
        self.framesTitles = ["Default", "ClockedInScreen", "AddTimeScreen", "PauseScreen"]
        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(AddTimeFrame)


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