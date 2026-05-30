import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#from services.week_service import WeekService


class GraphFrame(tk.Frame):
    def __init__(self, parent, controller, state):
        super().__init__(parent)
        self.parent = parent
        self.controller = controller

        button_frame = tk.Frame(self)
        button_frame.grid(row=1, column=0)
        table_frame = tk.Frame(self)
        table_frame.grid(row=0, column=0, padx=30, pady=(30, 0))  

        self.grid_rowconfigure(0, weight=1)
        #self.grid_rowconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=1)

        # --- GRAPH ---
        fig = Figure(figsize=(5, 3), dpi=80)
        ax = fig.add_subplot(111)
        ax.barh(["Stonks", "Devops", "Toil Tally", "Stons", "Devop", "Toi Tally", "Ston", "Devo", "Toi Taly"], [12, 8, 30, 12, 8, 30, 12, 8, 30])
        ax.set_xlabel("Hours")
        ax.set_title("Weekly Job Hours")

        fig.tight_layout()
        
        canvas = FigureCanvasTkAgg(fig, master=table_frame)
        canvas.draw()
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=0, sticky="nsew")

        self.button1 = tk.Button(button_frame, text=controller.graph_buttons[0], command= lambda: self.on_click_home(controller, state))
        self.button1.grid(row=1, column=0)
        self.button2 = tk.Button(button_frame, text=controller.graph_buttons[1], command= lambda: self.on_click_notes(controller, state))
        self.button2.grid(row=1, column=1)


        
    def on_click_notes(self, controller, state):
        controller.show_frame(controller.graph_pages[1], state)

    def on_click_home(self, controller, state):
        controller.show_frame(controller.graph_pages[0], state)
