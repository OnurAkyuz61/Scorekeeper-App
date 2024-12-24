from tkinter import Tk, PhotoImage
from login import LoginScreen
from utils import initialize_database
import sys

def main_application(username):
    from scorekeeper import Scorekeeper
    Scorekeeper(username)

root = Tk()
root.withdraw()

# Platforma göre simge ayarla
if sys.platform.startswith("win"):  # Windows için
    root.iconbitmap("assets/icons/scoreboard_icon.ico")
elif sys.platform == "darwin":  # macOS için
    icon_path = "assets/icons/scoreboard_icon.png"
    icon = PhotoImage(file=icon_path)
    root.iconphoto(True, icon)

# Veritabanını başlat ve giriş ekranını başlat
initialize_database()
LoginScreen(root, main_application)
root.mainloop()
