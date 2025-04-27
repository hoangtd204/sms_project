class Student:
    def __init__(self, student_id, name, age, major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major
 
    def to_dict(self):
         return{"student_id": self.student_id,
                "name"   : self.name,
                "age"    : self.age,
                "major"  : self.major
              }
    
    def to_console_string(self):
        return f"{self.student_id:<15}{self.name:<20}{self.age:<10}{self.major:<20}"