from database import init_db
from register import register
from login import login
from attendance import mark_attendance

def main():
    init_db()

    print("=== Attendance Management System ===")
    while True:
        print("\n1. Register\n2. Login\n3. Mark Attendance\n4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            register(username, password)

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            login(username, password)

        elif choice == "3":
            username = input("Enter username: ")
            status = input("Enter status (Present/Absent): ")
            mark_attendance(username, status)

        elif choice == "4":
            print("👋 Exiting system...")
            break

        else:
            print("⚠️ Invalid choice!")

if __name__ == "__main__":
    main()
