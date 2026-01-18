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
