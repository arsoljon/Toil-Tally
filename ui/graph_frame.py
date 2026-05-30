import tkinter as tk
from tkinter import ttk
from services.week_service import WeekService
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GraphFrame(tk.Frame):
    def __init__(self, parent, controller, state):
        super().__init__(parent)
        self.parent = parent
        self.controller = controller
        self.week_service = WeekService()

        self.jobs, self.hours = self.week_service.get_bar_info(state)

        button_frame = tk.Frame(self)
        button_frame.grid(row=1, column=0)
        table_frame = tk.Frame(self)
        table_frame.grid(row=0, column=0, padx=30, pady=(30, 0))  

        self.grid_rowconfigure(0, weight=1)
        #self.grid_rowconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=1)


        # --- GRAPH ---
        fig = Figure(figsize=(5, 3), dpi=80)
        self.ax = fig.add_subplot(111)
        self.bars = self.ax.barh(self.jobs, self.hours, picker=True)
        self.ax.set_xlabel("Hours")
        self.ax.set_title("Weekly Job Hours")

        fig.tight_layout()
        
        self.canvas = FigureCanvasTkAgg(fig, master=table_frame)
        self.canvas.draw()
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=0, column=0, sticky="nsew")
        # Connect click handler
        self.canvas.mpl_connect("pick_event", lambda pick_event: self.on_bar_click_notes(pick_event, controller, state))

        self.button1 = tk.Button(button_frame, text=controller.graph_buttons[0], command= lambda: self.on_click_home(controller, state))
        self.button1.grid(row=1, column=0)

    def refresh(self, state):
        #update the jobs shown if a new job is added to job_durations
        self.jobs, self.hours = self.week_service.get_bar_info(state)
        self.ax.clear()
        self.bars = self.ax.barh(self.jobs, self.hours, picker=True)
        self.ax.set_xlabel("Hours")
        self.ax.set_title("Weekly Job Hours")

        # Redraw canvas
        self.canvas.draw_idle()
        


    def on_bar_click_notes(self,event, controller, state):
        bar = event.artist
        # Find which bar was clicked
        index = list(self.bars).index(bar)
        job_name = self.jobs[index]
        state.current_job = job_name
        print(f"Clicked: {job_name}")
        controller.show_frame(controller.graph_pages[1], state)

    def on_click_home(self, controller, state):
        controller.show_frame(controller.graph_pages[0], state)
