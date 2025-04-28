from controllers.read_inf import students
from database.db import save_student
from models.student import Student
from validators.validate_inf import is_duplicate_student_id, validate_name, validate_major

import re


def create_student():
    # get_user_input_sid
    while True:
        sid = input("ID: ")
        pattern = r'^PH\d{5}$'
        if not re.match(pattern, sid):
            print("Invalid ID format. Please enter an ID with 8 alphanumeric characters.")
        elif is_duplicate_student_id(sid, students) or sid == '':
            print(
                "This student_id already exists or is empty. Please enter another ID :)")
        else:
            break

    # get_user_input_name
    while True:
        name = input("Name: ")
        if name == '' or name == ' ':
            print("This field cannot be left blank")
        elif validate_name(name):
            print("The name cannot be longer than 30 characters")
        else:
            break

    # get_user_input_age
    while True:
        try:
            age = int(input("Age: "))
            if 10 <= age <= 100:
                print("Correct")
                break
            else:
                print("Age must be between 10 and 100.")
        except ValueError:
            print("Please text an integer ")

    # get_user_input_major
    while True:
        major = input("Major: ")
        if validate_major(major):
            break
        else:
            print("The major you entered is incorrect")

    student = Student(sid, name, age, major)
    students.append(student)
    save_student(students)
    print("Successfully")
