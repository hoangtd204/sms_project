
from Controllers.config_input import BaseStudentHandler
from Database.config import save_student
from Models.student import Student
from Controllers.read_inf import students

class StudentCreator(BaseStudentHandler):
    def create(self, all_student_for_create):
        sid = self.get_valid_sid(students)
        name = self.get_valid_name()
        age = self.get_valid_age()
        major = self.get_valid_major()

        student = Student(sid, name, age, major)
        students.append(student)
        save_student(students)
        print("Added Successfully!")

    def update(self, all_student_for_create, current_student_id):
        print("This method is not applicable for creating a student.")

def create_student():
    all_student_for_create = students
    StudentCreator().create(all_student_for_create)

