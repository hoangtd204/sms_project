from Controllers.read_inf import students
from Database.config import save_student
from Validators.validate_inf import is_duplicate_student_id_update, validate_name, validate_major
import re


def find_student_obj_by_id(student_list, student_id):
    for student in student_list:
        if student.student_id == student_id:
            return student
    return None


def get_obj_to_update_student(student_list, target_student):

    while True:
        new_student_id = input('Enter the new student id: ')
        pattern = r'^PH\d{5}$'

        if not re.match(pattern, new_student_id):
            print("Invalid ID format. Please enter an ID like 'PHxxxxx'.")
        elif new_student_id == '' or is_duplicate_student_id_update(
            new_student_id, students, target_student.student_id
        ):
            print("This student_id already exists or is empty. Please enter another ID.")
        else:
            target_student.student_id = new_student_id
            break

    while True:
        new_name = input("Please enter your new name: ").strip()
        if not new_name:
            print("This field cannot be left blank.")
        elif validate_name(new_name):
            print("The name cannot be longer than 30 characters.")
        else:
            target_student.name = new_name
            break

    while True:
        try:
            age = int(input("Age: "))
            if 10 <= age <= 100:
                target_student.age = age
                break
            else:
                print("Age must be between 10 and 100.")
        except ValueError:
            print("Please enter an integer.")

    while True:
        new_major = input("Major: ")

        if validate_major(new_major):
            target_student.major = new_major
            break
        else:
            print("The major you entered is incorrect")

    save_student(student_list)
    print("Updated Successfully!")


def update_student():
    if not students:
        print("The system does not have any students.")
        return
    else:
        student_id = input("Enter the student ID you want to update: ")
        target_student = find_student_obj_by_id(students, student_id)

        if target_student:
            get_obj_to_update_student(students, target_student)
        else:
            print("The student ID you entered does not exist.")
