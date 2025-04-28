from models.student import Student
from controllers import (read_student, create_student,
                         search_students, update_student, delete_student)
from views.menu import display_menu


def main():
    while True:
        display_menu()
        choice = input("Your choice: \n")
        if choice == '1':
            students = read_student()
            print(f"{'Student ID':<15}{'Name':<20}{'Age':<10}{'Major':<20}")
            print("-" * 65)
            for student in students:
                print(student.to_console_string())
        elif choice == '2':
            create_student()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            search_students()
        elif choice == '0':
            break
        else:
            print("Invalidate choice.PLease try again!")


main()
