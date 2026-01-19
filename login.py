import sqlite3

def login(username, password):
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()

    conn.close()
    if user:
        print(f"✅ Login successful! Welcome {username}")
        return True
    else:
        print("❌ Invalid credentials")
        return False
