class Student:
    def __init__(self, name, registration_number, access_no):
      
        self.name = name
        self.registration_number = registration_number
        self.access_no = access_no

    def __str__(self):
       return f"Name:{self.name} Reg.NO:{self.registration_number} Access.NO:{self.access_no}"

name = input("Student's Name:")
registration_number = input("Reg Number:")
access_no = input("Access Number:")

student = Student(name, registration_number, access_no)

print(student)

