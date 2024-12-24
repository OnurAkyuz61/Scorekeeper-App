import tkinter as tk
from tkinter import messagebox
from utils import validate_user
from PIL import Image, ImageTk

class LoginScreen:
    def __init__(self, root, on_login_success):
        self.root = root
        self.on_login_success = on_login_success

        self.window = tk.Toplevel(self.root)
        self.window.title("Login")
        self.window.geometry("400x500")  # Boyut güncellendi
        self.window.configure(bg="#2c3e50")  # Arka plan rengi

        # FIRST logosunu ekle
        self.add_logo()

        # Kullanıcı giriş formu
        tk.Label(self.window, text="Username", font=("Arial", 12), bg="#2c3e50", fg="white").pack(pady=(10, 5))
        self.username_entry = tk.Entry(self.window, font=("Arial", 12), width=25)
        self.username_entry.pack(pady=5)

        tk.Label(self.window, text="Password", font=("Arial", 12), bg="#2c3e50", fg="white").pack(pady=5)
        self.password_entry = tk.Entry(self.window, show="*", font=("Arial", 12), width=25)
        self.password_entry.pack(pady=5)

        # Modern Login Butonu
        self.add_login_button()

        self.window.bind('<Return>', self.enter_key_pressed)

    def add_logo(self):
        """FIRST logosunu ortada göster."""
        try:
            logo_image = Image.open("assets/icons/FRC_Logo.png")  # Logo dosyasının yolu
            #logo_image = logo_image.resize((200, 100), Image.Resampling.LANCZOS)  # Logo boyutu ayarlandı
            logo_photo = ImageTk.PhotoImage(logo_image)

            logo_label = tk.Label(self.window, image=logo_photo, bg="#2c3e50")
            logo_label.image = logo_photo  # Referansı sakla
            logo_label.pack(pady=(30, 20))
        except FileNotFoundError:
            tk.Label(self.window, text="FIRST Logo Missing", font=("Arial", 10, "italic"), bg="#2c3e50", fg="red").pack()

    def add_login_button(self):
        """Modern tasarıma sahip Login butonunu ekler."""
        login_button = tk.Button(
            self.window,
            text="Login",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",  # Buton arka plan rengi (yeşil ton)
            fg="white",  # Yazı rengi
            activebackground="#45a049",  # Aktif olduğunda arka plan rengi
            activeforeground="white",  # Aktif olduğunda yazı rengi
            bd=0,  # Kenarlık kalınlığı
            relief="flat",  # Kenarlık stili
            command=self.login
        )
        login_button.pack(pady=20)
        login_button.configure(
            highlightbackground="#007BFF",  # Dış kenar için mavi ton
            highlightcolor="#007BFF",  # Odaklandığında kenarlık rengi
            highlightthickness=2  # Kenarlık kalınlığı
        )

    def login(self):
        """Giriş işlemi."""
        username = self.username_entry.get()
        password = self.password_entry.get()
        if validate_user(username, password):
            messagebox.showinfo("Success", "Login successful!")
            self.window.destroy()
            self.on_login_success(username)
        else:
            messagebox.showerror("Error", "Invalid username or password!")

    def enter_key_pressed(self, event):
        """Enter tuşuna basıldığında giriş işlemini tetikler."""
        self.login()
