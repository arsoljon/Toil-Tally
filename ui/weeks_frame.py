import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#from services.week_service import WeekService


class ViewWeeksFrame(tk.Frame):
    def __init__(self, parent, ui_controller, week_controller, state):
        super().__init__(parent)
        self.ui_controller = ui_controller
        self.week_controller = week_controller
        table_frame = tk.Frame(self)
        table_frame.grid(row=0, column=0, padx=30, pady=(30, 0))  
        button_frame = tk.Frame(self)
        button_frame.grid(row=1, column=0)

        self.tree = ttk.Treeview(
            table_frame,
            columns=(state.column_labels[0],
                     state.column_labels[1],
                     state.column_labels[2],
                     state.column_labels[3],
                     state.column_labels[4]),
            show="headings"
        )
        for label in state.column_labels:
            self.tree.column(label, width=67, anchor="e")    
            self.tree.heading(label, text=label.title())
        
        for week in state.all_weeks:
            self.tree.insert("", "end", values=(week["week_date"], week["job_count"], week["total_hours"], week["average"], week["top_job"]))

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=False)
        scrollbar.pack(side="right", fill="y")
        self.button1 = tk.Button(button_frame, text=ui_controller.viewWeeks_buttons[0], command= lambda: self.on_click_home(ui_controller, state))
        self.button1.grid(row=1, column=0)
        self.tree.bind("<Double-1>", lambda event: self.on_click_walmart(event, ui_controller, state))

    def on_click_walmart(self, event, ui_controller, state):
        item = self.tree.focus()
        values = self.tree.item(item, "values")
        print("Open details for:", values)
        ui_controller.show_frame(ui_controller.viewWeeks_pages[1], state)

    def on_click_home(self, ui_controller, state):
        ui_controller.show_frame(ui_controller.viewWeeks_pages[0], state)