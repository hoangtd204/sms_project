import re
def is_duplicate_student_id(student_id, students):
    return any(s.student_id == student_id for s in students)

