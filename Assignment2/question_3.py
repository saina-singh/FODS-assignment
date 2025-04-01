'''
Check if a number is an Armstrong number.
'''

# Function to check if a number is an Armstrong number
def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    return n == sum(int(digit) ** num_digits for digit in num_str)

# Example usage
number = 153
print("Is Armstrong:", is_armstrong(number))  # Output: True
