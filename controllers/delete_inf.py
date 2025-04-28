from controllers.read_inf import students
from database.db import save_student

def delete_student():
    get_sid_to_delete = input("Enter student id to delete: ")
    result = next((i for i in students if i.student_id == get_sid_to_delete), None)
    if result:
        students.remove(result)
        save_student(students)
        print("Deleted Successfully!")
    else :
        print("Student not found!")