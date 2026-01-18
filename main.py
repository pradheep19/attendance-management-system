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

system = AttendanceSystem()
system.add_student("101", "Rahul", "CSE")
print(system.list_students())

#attendance

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

    def mark_attendance(self, student_id, status):
        today = str(date.today())
        if student_id not in self.attendance:
            self.attendance[student_id] = {}
        self.attendance[student_id][today] = status

system = AttendanceSystem()
system.add_student("101", "Rahul", "CSE")
system.mark_attendance("101", "Present")
print(system.attendance)
