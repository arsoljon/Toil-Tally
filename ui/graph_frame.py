import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#from services.week_service import WeekService


class GraphFrame(tk.Frame):
    def __init__(self, parent, controller, state):
        super().__init__(parent)
        self.controller = controller


        table_frame = tk.Frame(self)
        table_frame.grid(row=0, column=0, padx=30, pady=(30, 0))  
        button_frame = tk.Frame(self)
        button_frame.grid(row=1, column=0)

        self.button1 = tk.Button(button_frame, text=controller.graph_buttons[0], command= lambda: self.on_click_home(controller, state))
        self.button1.grid(row=1, column=0)
        self.button2 = tk.Button(button_frame, text=controller.graph_buttons[1], command= lambda: self.on_click_notes(controller, state))
        self.button2.grid(row=1, column=1)

        
    def on_click_notes(self, controller, state):
        controller.show_frame(controller.graph_pages[1], state)

    def on_click_home(self, controller, state):
        controller.show_frame(controller.graph_pages[0], state)