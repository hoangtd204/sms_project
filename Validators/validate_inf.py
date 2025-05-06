
def is_duplicate_student_id(student_id, students):
    student_ids = {s.student_id for s in students}
    return student_id in student_ids


def is_duplicate_student_id_update(new_student_id, students, exclude_id):
    ids = {s.student_id for s in students if s.student_id != exclude_id}
    return new_student_id in ids



def validate_name(name):
    if len(name) > 30:
        return True
    else:
        return False

def validate_major(major_input):
    major_list = ["Biotechnology", "Graphic Design", "Data Science", "Software Engineering", "Cybersecurity", "Cloud Computing"]
    return any(major_input == major for major in major_list)
