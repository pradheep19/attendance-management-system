import sqlite3

def register(username, password):
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print(f"✅ User {username} registered successfully!")
    except sqlite3.IntegrityError:
        print("⚠️ Username already exists!")
    finally:
        conn.close()
