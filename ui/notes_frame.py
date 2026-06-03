import tkinter as tk
from tkinter import ttk
#from services.week_service import WeekService


class NotesFrame(tk.Frame):
    def __init__(self, parent, ui_controller, notes_controller, state):
        super().__init__(parent)
        self.ui_controller = ui_controller
        self.notes_controller = notes_controller

        table_frame = tk.Frame(self)
        table_frame.grid(row=0, column=0, padx=30, pady=(30, 0))  
        button_frame = tk.Frame(self)
        button_frame.grid(row=1, column=0)

        scrollbar = tk.Scrollbar(table_frame)
        scrollbar.pack(side="right", fill="y")

        self.text_box = tk.Text(table_frame, width=40, height = 10, yscrollcommand=scrollbar.set)
        self.text_box.pack(side="left", fill="both", expand=False)
        self.text_box.config(font=("Arial", 12), wrap="word", padx=10, pady=10)

        scrollbar.config(command=self.text_box.yview)

        self.button1 = tk.Button(button_frame, text=ui_controller.notes_buttons[0], command= lambda: self.on_click_graph(ui_controller, state))
        self.button1.grid(row=1, column=0)
        self.button2 = tk.Button(button_frame, text=ui_controller.notes_buttons[1], command= lambda: self.on_click_view_weeks(ui_controller, state))
        self.button2.grid(row=1, column=1)
        self.button3 = tk.Button(button_frame, text=ui_controller.notes_buttons[2], command= lambda: self.on_click_home(ui_controller, state))
        self.button3.grid(row=1, column=2)

        

    def on_click_graph(self, ui_controller, state):
        ui_controller.show_frame(ui_controller.notes_pages[0], state)

    def on_click_view_weeks(self, ui_controller, state):
        ui_controller.show_frame(ui_controller.notes_pages[1], state)

    def on_click_home(self, ui_controller, state):
        content = self.text_box.get(1.0, tk.END).strip()
        print("SAVED: ", content)
        ui_controller.show_frame(ui_controller.notes_pages[2], state)  