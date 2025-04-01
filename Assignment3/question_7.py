''''
A program to implement a class called employee with attributes such as empid, name, address, contact_number, spouse name, number_of_child, salary
'''
import csv

class Employee:
    """
    A class to represent an Employee with attributes such as empid, name, address, etc.
    """
    def __init__(self, empid, name, address, contact_number, spouse_name, number_of_child, salary):
        self.empid = empid
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.spouse_name = spouse_name
        self.number_of_child = number_of_child
        self.salary = salary

    def get_details(self):
        """
        Returns employee details as a list.
        """
        return [self.empid, self.name, self.address, self.contact_number, self.spouse_name, self.number_of_child, self.salary]

def write_to_csv(employee_list, filename="employees.csv"):
    """
    Writes the list of employees to a CSV file.
    """
    try:
        with open(filename, mode="w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            # Writing headers
            writer.writerow(["Employee ID", "Name", "Address", "Contact Number", "Spouse Name", "Number of Children", "Salary"])
            # Writing employee details
            for emp in employee_list:
                writer.writerow(emp.get_details())
        print(f"\nEmployee details successfully saved to {filename}!\n")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def read_from_csv(filename="employees.csv"):
    """
    Reads and displays the employee details from a CSV file.
    """
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            data = list(reader)

            if len(data) <= 1:
                print("\nNo employee records found!\n")
                return
            
            print("\n--- Employee List ---")
            for row in data:
                print(", ".join(row))

    except FileNotFoundError:
        print(f"\nError: The file '{filename}' was not found!\n")
    except Exception as e:
        print(f"\nAn error occurred while reading the file: {e}\n")

# Main program loop
employees = []
while True:
    try:
        print("\nEnter Employee Details:")
        empid = input("Employee ID: ")
        name = input("Name: ")
        address = input("Address: ")
        contact_number = input("Contact Number: ")
        spouse_name = input("Spouse Name (Enter 'None' if not applicable): ")
        number_of_child = int(input("Number of Children: "))
        salary = float(input("Salary: "))

        # Creating an Employee object and adding it to the list
        employee = Employee(empid, name, address, contact_number, spouse_name, number_of_child, salary)
        employees.append(employee)

        # Asking if the user wants to add more employees
        more = input("\nDo you want to add another employee? (yes/no): ").strip().lower()
        if more != 'yes':
            break
    except ValueError:
        print("\nError: Please enter valid numerical values for number of children and salary!\n")

# Write employee details to the file
write_to_csv(employees)

# Display the list of employees
read_from_csv()
