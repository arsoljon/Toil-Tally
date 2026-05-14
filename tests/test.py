from pywinauto import Application
import time

windowTitles = ["Default", "ClockedInScreen", "AddTimeScreen", "PauseScreen"]
currentDate = time.strftime("%Y-%m-%d")
totalTime = "01:23:45"
todaysTotalTime = "00:26:33"
prompt_currentDate = f"Date: {currentDate}"
prompt_totalTime = f"Total Time: {totalTime}"
prompt_todaysTotalTime = f"Accumulated Today: {todaysTotalTime}"

app = Application(backend="uia").start(
    r"pythonw main.py",
    wait_for_idle=False
)
dlg = app.window(title=windowTitles[0])
dlg.wait("visible", timeout=10)
dlg.print_control_identifiers()

statics = dlg.children(control_type="Text")
for s in dlg.descendants():
    print(s, repr(s.window_text()))


app.kill()