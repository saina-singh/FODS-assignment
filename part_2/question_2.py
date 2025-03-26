'''
Program to divide two numbers and display the result with exactly two decimal places.
'''

# Taking two integer inputs
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

# Checking for division by zero
if num2 == 0:
    print("Division by zero is not allowed.")
else:
    result = num1 / num2
    print(f"Result: {result:.2f}")
