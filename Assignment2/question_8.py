'''
Program to compare two lists based on length, sum, and common values.
'''

# Function to collect a list of integers
def get_integer_list(prompt):
    numbers = []
    while True:
        try:
            num = input(f"Enter a number for {prompt} (or type 'done' to finish): ")
            if num.lower() == 'done':
                break  # Stop taking inputs
            numbers.append(int(num))  # Convert input to integer and store it
        except ValueError:
            print("Invalid input! Please enter an integer.")
    return numbers

# Get two lists from user input
list1 = get_integer_list("List 1")
list2 = get_integer_list("List 2")

# Check if lists have the same length
if len(list1) == len(list2):
    print("Both lists have the same length.")
else:
    print("The lists have different lengths.")

# Check if the sums of the lists are the same
if sum(list1) == sum(list2):
    print("The sum of elements in both lists is the same.")
else:
    print("The sum of elements in both lists is different.")

# Check for common values
common_values = set(list1) & set(list2)
if common_values:
    print("Common values found in both lists:", common_values)
else:
    print("No common values found in both lists.")
