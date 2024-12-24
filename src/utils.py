import sqlite3
import os

def initialize_database():
    """Veritabanını başlatır ve kullanıcı tablosunu oluşturur."""
    os.makedirs("db", exist_ok=True)
    conn = sqlite3.connect("db/users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()

    # Varsayılan admin kullanıcısını ekle
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", "1234"))
        conn.commit()
    except sqlite3.IntegrityError:
        pass  # Eğer kullanıcı zaten varsa, atla

    conn.close()

def validate_user(username, password):
    """Kullanıcı giriş bilgilerini doğrular."""
    conn = sqlite3.connect("db/users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None
