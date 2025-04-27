from controllers.read_inf import students
from database.db import save_student
from validators.validate_inf import is_duplicate_student_id_for_update_inf
import sys
import os

def find_student_obj_by_id(student_list, student_id):
    for student in student_list:
        if student.student_id == student_id:
            return student
    return None

def get_obj_to_update_student(students,object_target_to_update):
     while True:
        newStudentId = input('Enter the new student id: ')
        if is_duplicate_student_id_for_update_inf:
           object_target_to_update.student_id= newStudentId
           save_student(students)
           break
        else:
            print("The student_id is already exists or empty!") 
     while True:
        newName=input("Please enter your new name:")
        if True:
           object_target_to_update.name= newName
           save_student(students)
           break
        else:
           print("")

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
