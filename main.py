from models.student import Student
from controllers import (read_student,create_student,search_students)
from views.menu import display_menu
def main():
    while True:
         display_menu()
         choice= input("Your choice: \n")
         if choice == '1':
             students = read_student()
             for i in students:
                 print(f"{i}")
         elif choice == '2':
             create_student()
             print("Added.")
         # elif choice == '3':
         #
         # elif choice == '4':
         #     pass
         elif choice == '5':
             search_students()
         # elif choice == '0':
         #     break
         else :
             print("Invalidate choice.PLease try again!")

main()