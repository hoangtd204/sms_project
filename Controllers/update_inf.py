from Controllers.read_inf import students
from Database.config import save_student
from Controllers.config_input import BaseStudentHandler


def find_student_obj_by_id(student_list, student_id):
    for student in student_list:
        if student.student_id == student_id:
            return student
    return None

#class update a student
class StudentUpdater(BaseStudentHandler):
    def update(self, student_list, target_student):
        target_student.student_id = self.get_valid_sid_to_update(student_list, target_student.student_id)
        target_student.name = self.get_valid_name()
        target_student.age = self.get_valid_age()
        target_student.major = self.get_valid_major()
        save_student(student_list)
        print("Updated Successfully!")

    def create(self,all_student_for_update):
        print("This method is not applicable for updating a student.")


def update_student():
    all_student_for_update = students
    if not students:
        print("The system does not have any students.")
        return
    else:
        student_id = input("Enter the student ID you want to update: ")
        target_student = find_student_obj_by_id(all_student_for_update, student_id)
        if target_student:
            StudentUpdater().update(all_student_for_update, target_student)
        else:
            print("The student ID you entered does not exist.")
