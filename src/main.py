import sys
import threading
from tkinter import Tk, PhotoImage
from login import LoginScreen
from utils import initialize_database
from web.app import app

def start_flask_app():
    app.run(debug=False, use_reloader=False)

def main_application(username):
    from scorekeeper import Scorekeeper
    Scorekeeper(username)

if __name__ == "__main__":
    flask_thread = threading.Thread(target=start_flask_app)
    flask_thread.daemon = True
    flask_thread.start()

    root = Tk()
    root.withdraw()

    if sys.platform.startswith("win"):
        root.iconbitmap("assets/icons/scoreboard_icon.ico")
    elif sys.platform == "darwin":
        icon_path = "assets/icons/scoreboard_icon.png"
        icon = PhotoImage(file=icon_path)
        root.iconphoto(True, icon)

    initialize_database()
    LoginScreen(root, main_application)
    root.mainloop()
