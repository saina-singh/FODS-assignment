'''
Program to convert Celsius to Fahrenheit.
Formula: F = (C * 9/5) + 32
'''

# Taking Celsius input from the user
celsius = float(input("Enter temperature in Celsius: "))

# Conversion
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")
