from controllers.read_inf import students

def search_students():
    keyword = input("Enter your keyword: ")
    result = next((obj for obj in students if obj.name.lower() == keyword.lower()), None)
    if result:
        print("Here's person who u r searching: \n", result)
    else:
        print("No one here in my list  ", keyword)
