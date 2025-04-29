import json
import os
from Models.student import Student


def get_json_path():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    json_path = os.path.join(dir_path, 'students_inf.json')
    return os.path.abspath(json_path)


# filepath
FILE_PATH = get_json_path()

# load student from json file


def load_students():
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Student(**item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        return []


def save_student(students):
    with open(FILE_PATH, 'w', encoding='utf-8') as f:
        json.dump([student.to_dict()
                  for student in students], f, indent=4, ensure_ascii=False)
