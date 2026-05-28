import tkinter as tk
from services.delete_service import DeleteService 
from services.state_service import StateService
import time

class HomeFrame(tk.Frame):
    def __init__(self, parent, controller, state):
        super().__init__(parent)
        self.controller = controller
        self.delete_service = DeleteService()
        self.state_service = StateService()
        self.selected = tk.StringVar(value="Other")

        #text
        self.label_currentDate = tk.Label(self, text=f"Date: {state.currentDate}", font=(controller.style, controller.size))
        self.label_currentDate.grid(row=0, column=0, sticky="w")
        self.label_totalTime = tk.Label(self, text=f"", font=(controller.style, controller.size))
        self.label_totalTime.grid(row=0, column=1, sticky="e")
        self.label_todaysTotalTime = tk.Label(self, text= f"", font=(controller.style, controller.size))
        self.label_todaysTotalTime.grid(row=2, column=0, sticky="w")
        #buttons
        self.button1 = tk.Button(self, text=controller.home_buttons[0], command=lambda: self.on_click_clock_in(controller, state))
        self.button1.grid(row=1, column=0, sticky="w")
        self.crud_frame = tk.Frame(self)
        self.crud_frame.grid(row=1, column=2)
        self.button2 = tk.Button(self.crud_frame, text=controller.home_buttons[1], command=lambda: self.on_click_add_data(controller, state))
        self.button2.grid(row=1, column=1, sticky="e")
        self.button3 = tk.Button(self.crud_frame, text=controller.home_buttons[2], command=lambda: self.on_click_delete(controller, state))
        self.button3.grid(row=1, column=2, sticky="swne")
        self.button4 = tk.Button(self.crud_frame, text=controller.home_buttons[3], command=lambda: self.on_click_undo(controller, state))
        self.button4.grid(row=1, column=3, sticky="e")
        self.button5 = tk.Button(self.crud_frame, text=controller.home_buttons[4], command=lambda: self.on_click_save(controller, state))
        self.button5.grid(row=2, column=2)

        self.radiobuttons_frame = tk.Frame(self)
        self.radiobuttons_frame.grid(row=1, column=1)
        
        self.refresh(state)

    def on_click_save(self, controller, state):
        self.state_service.update_state(controller, state)
        controller.destroy()


    def on_click_undo(self, controller, state):
        self.delete_service.undo_deletion(controller, state)
        controller.show_frame(controller.home_pages[2], state)

    def on_click_delete(self, controller, state):
        #state.currentJob = f"{self.selected.get()}"
        #controller.show_frame(controller.home_pages[0], state)
        self.delete_service.delete_job(controller, state, self.selected.get())
        self.selected.set("Other")
        controller.show_frame(controller.home_pages[2], state)

    def on_click_clock_in(self, controller, state):
        #clockIn
        if self.selected.get().lower() == "other":
            return
        state.currentJob = f"{self.selected.get()}"
        self.state_service.update_session_initial(state)
        controller.show_frame(controller.home_pages[0], state)

    def on_click_add_data(self, controller, state):
        #manually add to job
        state.currentJob = f"{self.selected.get()}"
        controller.show_frame(controller.home_pages[1], state)
    
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
        
