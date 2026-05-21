import tkinter as tk

class HomeFrame(tk.Frame):
    def __init__(self, parent, controller, state):
        super().__init__(parent)
        self.controller = controller
        self.currentDate = state.currentDate
        self.totalTime = state.totalTime
        self.todaysTotalTime = state.todaysTotalTime
        self.buttonLabels = controller.home_buttons
        self.pages = controller.home_pages
        style = state.style
        size = state.size
        self.selected = tk.StringVar(value="Other")

        #text
        self.label_currentDate = tk.Label(self, text=f"Date: {state.currentDate}", font=(state.style, state.size))
        self.label_currentDate.grid(row=0, column=0, sticky="w")
        self.label_totalTime = tk.Label(self, text=f"Total Time {state.totalTime}", font=(state.style, state.size))
        self.label_totalTime.grid(row=0, column=1, sticky="e")
        self.label_todaysTotalTime = tk.Label(self, text= f"Todays Total: {state.todaysTotalTime}", font=(state.style, state.size))
        self.label_todaysTotalTime.grid(row=2, column=0, sticky="w")
        #buttons
        self.button1 = tk.Button(self, text=controller.home_buttons[0], command=lambda: self.on_click(controller, controller.home_buttons[0], state))
        self.button1.grid(row=1, column=0, sticky="w")
        self.button2 = tk.Button(self, text=controller.home_buttons[1], command=lambda: self.on_click(controller, controller.home_buttons[1], state))
        self.button2.grid(row=1, column=1, sticky="e")
        #radioButtons
        labels_jobs = state.labels_for_jobs
        self.radioButtons = []
        for i, job in enumerate(labels_jobs):
            rb = tk.Radiobutton(
                self,
                text=job,
                variable=self.selected,
                value=job
            )
            rb.grid(row=i+1, column= 1)
            self.radioButtons.append(rb)
        self.refresh(state)

    def on_click(self, controller, buttonLabel, state):
        if(buttonLabel == controller.home_buttons[0]):
            #clockIn
            print(f"{controller.home_buttons[0]} : {self.selected.get()}!")
            state.currentJob = f"{self.selected.get()}"
            controller.show_frame(controller.home_pages[0], state)
        else:
            #manually add to job
            state.job_selected = self.selected.get()
            print(f"{controller.home_buttons[1]} : selected {self.selected.get()}, !")
            controller.show_frame(controller.home_pages[1], state)
    
    def refresh(self, state):
        #radiobuttons
        print(self.selected.get())
        
