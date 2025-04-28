import re
def is_duplicate_student_id(student_id, students):
    return any(s.student_id == student_id for s in students)

def is_duplicate_student_id_for_update_inf(student_id, students):
   return not any(s.student_id == student_id for s in students)

def validate_name(name):
    if len(name) > 30:
        return True
    else:
        return False


def validate_major(major_input):
    major_list = ["Biotechnology", "Graphic Design", "Data Science", "Software Engineering", "Cybersecurity","Cloud Computing"]
    for major in major_list:
        if major_input == major :
            return True
    return False