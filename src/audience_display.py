import tkinter as tk
import sys

class AudienceDisplay:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Audience Display")
        self.window.geometry("1280x720")
        self.window.configure(bg="fuchsia")

        # Uygulama simgesi ekle
        self.set_window_icon()

        # UI Bileşenlerini oluştur
        self.init_ui()

    def set_window_icon(self):
        if sys.platform.startswith("win"):
            self.window.iconbitmap("assets/icons/scoreboard_icon.ico")
        elif sys.platform == "darwin":
            icon_path = "assets/icons/scoreboard_icon.png"
            icon = tk.PhotoImage(file=icon_path)
            self.window.iconphoto(True, icon)

    def init_ui(self):
        footer_frame = tk.Frame(self.window, bg="black", height=240)
        footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Timer ve Skorlar
        tk.Label(footer_frame, text="Audience Display", font=("Arial", 16), fg="white", bg="black").pack(pady=20)

    def update_scores(self, red_score, blue_score):
        pass

    def update_timer(self, time_left):
        pass
