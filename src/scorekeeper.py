import tkinter as tk
import sys
from audience_display import AudienceDisplay

class Scorekeeper:
    def __init__(self, username):
        self.username = username
        self.audience_display = None

        self.window = tk.Toplevel()
        self.window.title("Scorekeeper - Developed by Onur Akyüz")
        self.window.geometry("400x500")

        # Uygulama simgesi ekle
        self.set_window_icon()

        # UI Bileşenlerini başlat
        self.init_ui()

    def set_window_icon(self):
        if sys.platform.startswith("win"):
            self.window.iconbitmap("assets/icons/scoreboard_icon.ico")
        elif sys.platform == "darwin":
            icon_path = "assets/icons/scoreboard_icon.png"
            icon = tk.PhotoImage(file=icon_path)
            self.window.iconphoto(True, icon)

    def init_ui(self):
        tk.Label(self.window, text=f"Welcome to Scorekeeper!", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.window, text="Open Audience Display", command=self.open_audience_display).pack(pady=10)

        # Skor ve timer kontrolü
        tk.Button(self.window, text="Red +10", command=lambda: self.update_score("red", 10)).pack(pady=5)
        tk.Button(self.window, text="Blue +10", command=lambda: self.update_score("blue", 10)).pack(pady=5)
        tk.Button(self.window, text="Set Timer to 1:30", command=lambda: self.set_timer("1:30")).pack(pady=5)

    def open_audience_display(self):
        if not self.audience_display:
            self.audience_display = AudienceDisplay()
        else:
            self.audience_display.window.deiconify()

    def update_score(self, team, points):
        if self.audience_display:
            current_red = int(self.audience_display.red_score_label.cget("text"))
            current_blue = int(self.audience_display.blue_score_label.cget("text"))
            if team == "red":
                self.audience_display.update_scores(current_red + points, current_blue)
            elif team == "blue":
                self.audience_display.update_scores(current_red, current_blue + points)

    def set_timer(self, time_left):
        if self.audience_display:
            self.audience_display.update_timer(time_left)
