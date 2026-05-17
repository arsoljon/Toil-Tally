import tkinter as tk
from tkinter import font
import time


class HomeFrame(tk.Frame):
    def __init__(self, parent, controller, clockInPage, addPage, totalTime, currentDate):
        super().__init__(parent)
        self.todaysTotalTime = "00:26:33"
        self.buttonLabels = ["Start", "Add"]
        self.pages = [clockInPage, addPage]
        style = "Arial"
        size_offset = .8
        size = int(16 * size_offset)

        #text
        self.label_currentDate = tk.Label(self, text=f"Date: {currentDate}", font=(style, size))
        self.label_currentDate.grid(row=0, column=0, sticky="w")
        self.label_totalTime = tk.Label(self, text=f"Total Time {totalTime}", font=(style, size))
        self.label_totalTime.grid(row=0, column=1, sticky="e")
        self.label_todaysTotalTime = tk.Label(self, text= f"Todays Total: {self.todaysTotalTime}", font=(style, size))
        self.label_todaysTotalTime.grid(row=2, column=0, sticky="w")
        #buttons
        self.button1 = tk.Button(self, text=self.buttonLabels[0], command=lambda: controller.show_frame(self.pages[0]))
        self.button1.grid(row=1, column=0, sticky="w")
        self.button2 = tk.Button(self, text=self.buttonLabels[1], command=lambda: controller.show_frame(self.pages[1]))
        self.button2.grid(row=1, column=1, sticky="e")

    def on_click(self):
        print()
        buttonMessage = "Button clicked!"
        print(buttonMessage)

    def getButtons(self):
        return self.buttonLabels
    def getTodaysTotalTime(self):
        return self.todaysTotalTime

class ClockedInFrame(tk.Frame):
    def __init__(self, parent, controller, totalTime, currentDate):
        super().__init__(parent)
        self.lengthOfSession = "01:02:03"
        self.buttonLabels = ["End", "Pause"]
        #text
        style = "Arial"
        size_offset = .8
        size = int(16 * size_offset)
        
        self.label_currentDate = tk.Label(self, text=f"Date: {currentDate}", font=(style, size))
        self.label_currentDate.grid(row=0, column=0, sticky="w")
        self.label_totalTime = tk.Label(self, text=f"Total Time: {totalTime}", font=(style, size))
        self.label_totalTime.grid(row=0, column=1, sticky="ne")

        self.label_lengthOfSession = tk.Label(self, text= f"Total: {self.lengthOfSession}", font=("Arial", 16))
        self.label_lengthOfSession.grid(row=2, column=0)
        #buttons
        self.button1 = tk.Button(self, text=self.buttonLabels[0], command= lambda: self.on_click(controller, self.buttonLabels[0]))
        self.button1.grid(row=1, column=0)
        self.button2 = tk.Button(self, text=self.buttonLabels[1], command= lambda: self.on_click(controller, self.buttonLabels[1]))
        self.button2.grid(row=1, column=1)

    def on_click(self, controller, buttonLabel):
        if(buttonLabel == self.buttonLabels[0]):
            print(f"{self.buttonLabels[0]}!")
            controller.show_frame(HomeFrame)
        else:
            print(f"{self.buttonLabels[1]}!")
            controller.show_frame(PauseFrame)

    def getButtons(self):
        return self.buttonLabels
    def getLengthOfSession(self):
        return self.lengthOfSession

class AddTimeFrame(tk.Frame):
    def __init__(self, parent, controller, totalTime, currentDate):
        super().__init__(parent)
        self.timeSelection= "00:00:00"
        self.buttonLabels = ["Add", "Cancel"]
        #text
        style = "Arial"
        size_offset = .8
        size = int(16 * size_offset)

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
        self.button1 = tk.Button(self, text=self.buttonLabels[0], command= lambda: self.on_click(controller, self.buttonLabels[0]))
        self.button1.grid(row=1, column=0)
        self.button2 = tk.Button(self, text=self.buttonLabels[1], command= lambda: self.on_click(controller, self.buttonLabels[1]))
        self.button2.grid(row=2, column=0)

    def on_click(self, controller, buttonLabel):
        if(buttonLabel == self.buttonLabels[0]):
            print(f"{self.buttonLabels[0]}!")
            controller.show_frame(HomeFrame)
        else:
            print(f"{self.buttonLabels[1]}!")
            controller.show_frame(HomeFrame)

    def getButtons(self):
        return self.buttonLabels
    def getTimeSelection(self):
        return self.timeSelection

class PauseFrame(tk.Frame):
    def __init__(self, parent, controller, sessionLength, totalTime, currentDate):
        super().__init__(parent)
        self.lengthOfSession = sessionLength
        self.lengthOfPauseSession = "00:00:00"
        self.buttonLabels = ["End", "Continue"]
        #text preprocessing
        root = self.winfo_toplevel()
        root.update_idletasks()

        #text
        style = "Arial"
        size_offset = .8
        size = int(16 * size_offset)
        my_text = font.Font(family=style, size=size)

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
        self.button1 = tk.Button(self, text=self.buttonLabels[0], command= lambda: self.on_click(controller, self.buttonLabels[0]))
        self.button1.grid(row=1, column=0)
        self.button2 = tk.Button(self, text=self.buttonLabels[1], command= lambda: self.on_click(controller, self.buttonLabels[1]))
        self.button2.grid(row=1, column=1)
 
    def on_click(self, controller, buttonLabel):
        if(buttonLabel == self.buttonLabels[0]):
            print(f"{self.buttonLabels[0]}!")
            controller.show_frame(HomeFrame)
        else:
            print(f"{self.buttonLabels[1]}!")
            controller.show_frame(ClockedInFrame)

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
        self.frames[HomeFrame] = HomeFrame(container, self, ClockedInFrame, AddTimeFrame, self.totalTime, self.currentDate)
        self.frames[ClockedInFrame] = ClockedInFrame(container, self, self.totalTime, self.currentDate)
        session_length = self.frames[ClockedInFrame].getLengthOfSession()
        self.frames[PauseFrame] = PauseFrame(container, self, session_length, self.totalTime, self.currentDate)
        self.frames[AddTimeFrame] = AddTimeFrame(container, self, self.totalTime, self.currentDate)
        self.framesTitles = ["Default", "ClockedInScreen", "AddTimeScreen", "PauseScreen"]
        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(HomeFrame)

    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()
        
        
if __name__ == "__main__":
    app = AppUI()
    app.mainloop()