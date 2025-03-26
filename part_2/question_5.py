'''
Program to calculate simple interest.
Formula: SI = (P * R * T) / 100
'''

# Taking user input
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time period in years: "))

# Calculating simple interest
interest = (principal * rate * time) / 100
print(f"Simple Interest: {interest:.2f}")
