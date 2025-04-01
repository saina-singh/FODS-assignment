'''
Calculator program to perform basic arithmetic operations.
'''

# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    return a / b if b != 0 else "Error: Division by zero"

# Function for truncated division (floor division)
def truncated_division(a, b):
    return a // b if b != 0 else "Error: Division by zero"

# Function for modulus
def modulus(a, b):
    return a % b if b != 0 else "Error: Division by zero"

# Function for exponentiation
def exponentiate(a, b):
    return a ** b

# Example usage
num1, num2 = 10.5, 2.0
print("Addition:", add(num1, num2))          # Output: 12.5
print("Subtraction:", subtract(num1, num2))  # Output: 8.5
print("Multiplication:", multiply(num1, num2))  # Output: 21.0
print("Division:", divide(num1, num2))       # Output: 5.25
print("Truncated Division:", truncated_division(num1, num2))  # Output: 5.0
print("Modulus:", modulus(num1, num2))       # Output: 0.5
print("Exponentiation:", exponentiate(num1, num2))  # Output: 110.25
