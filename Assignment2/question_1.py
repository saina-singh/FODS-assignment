'''
Counts uppercase and lowercase letters in a string.
'''

# Function to count uppercase and lowercase letters
def count_case_letters(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

# Example usage
string = "Hello World!"
upper, lower = count_case_letters(string)
print("Uppercase Letters:", upper)  # Output: 2
print("Lowercase Letters:", lower)  # Output: 8
