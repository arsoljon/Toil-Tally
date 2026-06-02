import tkinter as tk

class HomeFrame(tk.Frame):
    def __init__(self, parent, ui_controller, home_controller, state):
        super().__init__(parent)
        self.ui_controller = ui_controller
        self.home_controller = home_controller
        self.selected = tk.StringVar(value="Other")

        #text
        self.label_currentDate = tk.Label(self, text=f"Date: {state.currentDate}", font=(ui_controller.style, ui_controller.size))
        self.label_currentDate.grid(row=0, column=0, sticky="w")
        self.label_totalTime = tk.Label(self, text=f"", font=(ui_controller.style, ui_controller.size))
        self.label_totalTime.grid(row=0, column=1, sticky="e")
        self.label_todaysTotalTime = tk.Label(self, text= f"", font=(ui_controller.style, ui_controller.size))
        self.label_todaysTotalTime.grid(row=2, column=0, sticky="w")
        #buttons
        self.button1 = tk.Button(self, text=ui_controller.home_buttons[0], command=lambda: self.on_click_clock_in(ui_controller, state))
        self.button1.grid(row=1, column=0, sticky="w")
        self.crud_frame = tk.Frame(self)
        self.crud_frame.grid(row=1, column=2)
        self.button2 = tk.Button(self.crud_frame, text=ui_controller.home_buttons[1], command=lambda: self.on_click_add_data(ui_controller, state))
        self.button2.grid(row=1, column=1, sticky="e")
        self.button3 = tk.Button(self.crud_frame, text=ui_controller.home_buttons[2], command=lambda: self.on_click_delete(ui_controller, state))
        self.button3.grid(row=1, column=2, sticky="swne")
        self.button4 = tk.Button(self.crud_frame, text=ui_controller.home_buttons[3], command=lambda: self.on_click_undo(ui_controller, state))
        self.button4.grid(row=1, column=3, sticky="e")
        self.button5 = tk.Button(self.crud_frame, text=ui_controller.home_buttons[4], command=lambda: self.on_click_save(ui_controller, state))
        self.button5.grid(row=2, column=2)
        self.button6 = tk.Button(self.crud_frame, text=ui_controller.home_buttons[5], command=lambda: self.on_click_view_weeks(ui_controller, state))
        self.button6.grid(row=4, column=2)

        self.radiobuttons_frame = tk.Frame(self)
        self.radiobuttons_frame.grid(row=1, column=1)
        
        self.refresh(state)

    def on_click_view_weeks(self, ui_controller, state):
        ui_controller.show_frame(ui_controller.home_pages[3], state)

    def on_click_save(self, ui_controller, state):
        self.home_controller.update_state()
        ui_controller.destroy()


    def on_click_undo(self, ui_controller, state):
        self.home_controller.undo_delete()
        ui_controller.show_frame(ui_controller.home_pages[2], state)

    def on_click_delete(self, ui_controller, state):
        self.home_controller.delete_job(self.selected.get())
        self.selected.set("Other")
        ui_controller.show_frame(ui_controller.home_pages[2], state)

    def on_click_clock_in(self, ui_controller, state):
        #clockIn
        if self.selected.get().lower() == "other":
            return
        state.currentJob = f"{self.selected.get()}"
        self.home_controller.update_session_initial()
        ui_controller.show_frame(ui_controller.home_pages[0], state)

    def on_click_add_data(self, ui_controller, state):
        #manually add to job
        state.currentJob = f"{self.selected.get()}"
        ui_controller.show_frame(ui_controller.home_pages[1], state)
    
    def refresh(self, state):
        for widget in self.radiobuttons_frame.winfo_children():
            widget.destroy()
        #radiobuttons
        labels_jobs = state.labels_for_jobs
        self.radioButtons = []
        for i, job in enumerate(labels_jobs):
            rb = tk.Radiobutton(
                self.radiobuttons_frame,
                text=job,
                variable=self.selected,
                value=job
            )
            rb.grid(row=i+1, column= 1, sticky="w")
            self.radioButtons.append(rb)
        other_radioButton = tk.Radiobutton(self.radiobuttons_frame, text="Other", variable=self.selected, value="Other")
        other_radioButton.grid(row=len(labels_jobs)+1, column=1, sticky="w")
        self.radioButtons.append(other_radioButton)
        self.label_totalTime.config(text=f"Total Time {state.totalTime}")
        self.label_todaysTotalTime.config(text=f"Todays Total: {state.todaysTotalTime}")
        
