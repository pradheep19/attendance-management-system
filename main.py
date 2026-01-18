from datetime import date

class AttendanceSystem:
    def __init__(self):
        self.students = {}
        self.attendance = {}

    def add_student(self, student_id, name, department):
        self.students[student_id] = {
            "name": name,
            "department": department
        }

    def list_students(self):
        return self.students

    def mark_attendance(self, student_id, status):
        today = str(date.today())
        if student_id not in self.attendance:
            self.attendance[student_id] = {}
        self.attendance[student_id][today] = status


# ---- USING THE SYSTEM ----
system = AttendanceSystem()

system.add_student("101", "Rahul", "CSE")
print("Students:", system.list_students())

system.mark_attendance("101", "Present")
print("Attendance:", system.attendance)