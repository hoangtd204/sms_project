from abc import ABC, abstractmethod
from Validators.validate_inf import is_duplicate_student_id, validate_name, validate_major,is_duplicate_student_id_update
import re


class BaseStudentHandler(ABC):
    #Option one for the Abtract method in this class
      @abstractmethod
      def create(self, students):
        pass

      @abstractmethod
      def update(self, students, current_student_id):
        pass

      @staticmethod
      def get_valid_sid(students):
          while True:
              sid = input("ID: ")
              pattern = r'^PH\d{5}$'
              if not re.match(pattern, sid):
                  print("Invalid ID format. Please enter an ID with 8 alphanumeric characters.")
              elif is_duplicate_student_id(sid, students) or sid == '':
                  print(
                      "This student_id already exists or is empty. Please enter another ID :)")
              else:
                return sid

      @staticmethod
      def get_valid_sid_to_update(students, current_id):
          while True:
              new_student_id = input('Enter the new student id: ')
              pattern = r'^PH\d{5}$'
              if not re.match(pattern, new_student_id):
                  print("Invalid ID format. Please enter an ID like 'PHxxxxx'.")
              elif new_student_id == '' or is_duplicate_student_id_update(
                      new_student_id, students,current_id):
                  print("This student_id already exists or is empty. Please enter another ID.")
              else:
                 return new_student_id

      @staticmethod
      def get_valid_name():
          while True:
              name = input("Name: ").strip()
              if not name:
                  print("This field cannot be left blank")
              elif validate_name(name):
                  print("The name cannot be longer than 30 characters")
              else:
                  return name

      @staticmethod
      def get_valid_age():
          while True:
              try:
                  age = int(input("Age: "))
                  if 10 <= age <= 100:
                      return age
                  else:
                      print("Age must be between 10 and 100.")
              except ValueError:
                  print("Please enter an integer")

      @staticmethod
      def get_valid_major():
          while True:
              major = input("Major: ")
              if validate_major(major):
                  return major
              else:
                  print("The major you entered is incorrect")


