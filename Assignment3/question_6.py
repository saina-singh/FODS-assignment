'''
A program to implement a class called employee with attributes such as empid, name, address, contact_number, spouse name, number_of_child, salary
'''
class Student:
    def __init__(self, student_id, name, address, admission_year, level, section):
        """
        Constructor to initialize student attributes.
        """
        self.student_id = student_id
        self.name = name
        self.address = address
        self.admission_year = admission_year
        self.level = level
        self.section = section

    def display_info(self):
        """
        Method to display student details.
        """
        print("\n--- Student Details ---")
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Admission Year: {self.admission_year}")
        print(f"Level: {self.level}")
        print(f"Section: {self.section}")

# Taking input from the user
student_id = input("Enter Student ID: ")
name = input("Enter Name: ")
address = input("Enter Address: ")
admission_year = input("Enter Admission Year: ")
level = input("Enter Level: ")
section = input("Enter Section: ")

# Creating an instance of Student
student1 = Student(student_id, name, address, admission_year, level, section)

# Displaying student details
student1.display_info()
