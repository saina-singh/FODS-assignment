'''
Program to count the number of letters and digits in a given string.
'''

# Taking input from user
text = input("Enter a string: ")

# Initializing counters
letters = sum(c.isalpha() for c in text)
digits = sum(c.isdigit() for c in text)

# Displaying results
print(f"Letters: {letters}")
print(f"Digits: {digits}")
