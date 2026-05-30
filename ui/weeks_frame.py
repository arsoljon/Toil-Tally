import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#from services.week_service import WeekService


class ViewWeeksFrame(tk.Frame):
    def __init__(self, parent, controller, state):
        super().__init__(parent)
        self.controller = controller


        table_frame = tk.Frame(self)
        table_frame.grid(row=0, column=0, padx=30, pady=(30, 0))  
        button_frame = tk.Frame(self)
        button_frame.grid(row=1, column=0)

        self.tree = ttk.Treeview(
            table_frame,
            columns=("job", "hours"),
            show="headings"
        )

        self.tree.heading("job", text="Job")
        self.tree.heading("hours", text="Hours")

        for i in range(20):
            self.tree.insert("", "end", values=("Walmart", 12))
            self.tree.insert("", "end", values=("Target", 8))
        
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=False)
        scrollbar.pack(side="right", fill="y")
        self.button1 = tk.Button(button_frame, text=controller.viewWeeks_buttons[0], command= lambda: self.on_click_home(controller, state))
        self.button1.grid(row=1, column=0)
        self.tree.bind("<Double-1>", lambda event: self.on_click_walmart(event, controller, state))

    def on_click_walmart(self, event, controller, state):
        item = self.tree.focus()
        values = self.tree.item(item, "values")
        print("Open details for:", values)
        controller.show_frame(controller.viewWeeks_pages[1], state)

    def on_click_home(self, controller, state):
        controller.show_frame(controller.viewWeeks_pages[0], state)