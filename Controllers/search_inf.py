from Controllers.read_inf import students


class StudentFinder:
    @staticmethod
    def search(keyword):
        result = next((i for i in students if i.student_id == keyword), None)
        if result:
            print(
                f"Here's the person you are searching for:\n Student id: {result.student_id}  Name: {result.name}  Age: {result.age}  Major: {result.major}")
        else:
            print(f"No student found with ID: {keyword}")


def search_students():
    keyword = input("Enter student id to search: ")
    finder = StudentFinder()
    finder.search(keyword)



