import sqlite3
from datetime import date

def mark_attendance(username, status="Present"):
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE username=?", (username,))
    user = cursor.fetchone()

    if user:
        cursor.execute("INSERT INTO attendance (user_id, date, status) VALUES (?, ?, ?)",
                       (user[0], str(date.today()), status))
        conn.commit()
        print(f"✅ Attendance marked for {username} as {status}")
    else:
        print("⚠️ User not found!")

    conn.close()
