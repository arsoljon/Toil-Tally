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
            columns=("week", "job count", "total hours", "average", "top job"),
            show="headings"
        )
        self.tree.column("week", width=60)
        self.tree.column("job count", width=75)
        self.tree.column("total hours", width=90)
        self.tree.column("average", width=70)
        self.tree.column("top job", width=100)

        self.tree.heading("week", text="Week")
        self.tree.heading("job count", text="Job Count")
        self.tree.heading("total hours", text="Total Hours")
        self.tree.heading("average", text="Average")
        self.tree.heading("top job", text="Top Job")

        for i in range(20):
            self.tree.insert("", "end", values=("Walmart", 12, 2, 3,4))
            self.tree.insert("", "end", values=("Target", 12, 2, 3,4))
        
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