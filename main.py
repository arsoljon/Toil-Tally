import tkinter as tk
import time

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

default.mainloop()
