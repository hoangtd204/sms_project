from controllers.read_inf import students



def search_students():
    keyword = input("Enter student id to search: ")
    result = next((i for i in students  if i.student_id == keyword), None)


    if result:
        print(f"Here's person who u r searching:\n Student id:{result.student_id}  Name:{result.name}  Age:{result.age}  Major:{result.major}")
    else:
        print("No one here in my list  ", keyword)



