from controllers.read_inf import students
from database.db import save_student
from validators.validate_inf import is_duplicate_student_id
from validators.validate_inf import validate_name
import re

def find_student_obj_by_id(student_list, student_id):
    for student in student_list:
        if student.student_id == student_id:
            return student
    return None

def get_obj_to_update_student(students_to_update_original,object_target_to_update):

     student_to_update = students_to_update_original
    #get_input_to_update_sid
     while True:
        new_student_id = input('Enter the new student id: ')
        pattern = r'^PH\d{5}$'
        if not re.match(pattern, new_student_id):
            print("Invalid ID format. Please enter an ID with 8 alphanumeric characters.")
        elif is_duplicate_student_id(new_student_id, students) or new_student_id == '':
            print(
                "This student_id already exists or is empty. Please enter another ID :)")
        else:
            break
     # get_input_to_update_name
     while True:
        new_name=input("Please enter your new name:")
        if new_name == '' or new_name == ' ':
            print("This field cannot be left blank")
        elif validate_name(new_name):
            print("The name cannot be longer than 30 characters")
        else:
            find_student_obj_by_id.name = new_name
            save_student(student_to_update)
            break

     # get_input_to_update_sid
     while True:
         try:
             age = int(input("Age: "))
             if 10 <= age <= 100:
                 save_student(student_to_update)
                 break
             else:
                 print("Age must be between 10 and 100.")
         except ValueError:
             print("Please text an integer ")


def update_student():
    student_to_update=students
    if not student_to_update:
        return f"The system does not have any student to find"
    else:
        student_id = input("Enter the student ID you want to update: ")
        obj_target_to_update=find_student_obj_by_id(student_to_update,student_id)
        if obj_target_to_update:
          get_obj_to_update_student(student_to_update,obj_target_to_update)
        else:
         return f"The student ID you entered is not here"
