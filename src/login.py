import tkinter as tk
from tkinter import messagebox
from utils import validate_user
import sys

class LoginScreen:
    def __init__(self, root, on_login_success):
        self.root = root
        self.on_login_success = on_login_success

        self.window = tk.Toplevel(self.root)
        self.window.title("Login")
        self.window.geometry("300x200")
        self.window.configure(bg="#2c3e50")

        # Uygulama simgesi ekle
        self.set_window_icon()

        tk.Label(self.window, text="Username:", bg="#2c3e50", fg="white").pack(pady=5)
        self.username_entry = tk.Entry(self.window)
        self.username_entry.pack(pady=5)

        tk.Label(self.window, text="Password:", bg="#2c3e50", fg="white").pack(pady=5)
        self.password_entry = tk.Entry(self.window, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.window, text="Login", command=self.login).pack(pady=10)
        self.window.bind('<Return>', self.enter_key_pressed)

    def set_window_icon(self):
        if sys.platform.startswith("win"):
            self.window.iconbitmap("assets/icons/scoreboard_icon.ico")
        elif sys.platform == "darwin":
            icon_path = "assets/icons/scoreboard_icon.png"
            icon = tk.PhotoImage(file=icon_path)
            self.window.iconphoto(True, icon)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if validate_user(username, password):
            messagebox.showinfo("Success", "Login successful!")
            self.window.destroy()
            self.on_login_success(username)
        else:
            messagebox.showerror("Error", "Invalid username or password!")

    def enter_key_pressed(self, event):
        self.login()
