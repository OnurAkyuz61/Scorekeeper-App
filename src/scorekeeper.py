import tkinter as tk
from audience_display import AudienceDisplay

class Scorekeeper:
    def __init__(self, username):
        self.username = username
        self.audience_display = None

        self.window = tk.Toplevel()
        self.window.title("Scorekeeper")
        self.window.geometry("400x500")

        self.init_ui()

    def init_ui(self):
        tk.Label(self.window, text=f"Welcome, {self.username}!", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.window, text="Open Audience Display", command=self.open_audience_display).pack(pady=10)

        tk.Button(self.window, text="Red +10", command=lambda: self.update_score("red", 10)).pack(pady=5)
        tk.Button(self.window, text="Blue +10", command=lambda: self.update_score("blue", 10)).pack(pady=5)
        tk.Button(self.window, text="Set Timer to 1:30", command=lambda: self.set_timer("1:30")).pack(pady=5)

    def open_audience_display(self):
        if not self.audience_display:
            self.audience_display = AudienceDisplay()
        else:
            self.audience_display.window.deiconify()

    def update_score(self, team, points):
        pass

    def set_timer(self, time_left):
        pass
