'''
Program to accept integers and store only values between 1 and 100.
'''

# Function to collect valid integers
def collect_valid_numbers():
    numbers = []
    while True:
        try:
            num = input("Enter an integer (or type 'done' to finish): ")
            if num.lower() == 'done':
                break  # Exit the loop if user types 'done'
            num = int(num)  # Convert input to integer
            if 1 <= num <= 100:
                numbers.append(num)  # Add to list if within range
            else:
                print("Number out of range (1-100), not added.")
        except ValueError:
            print("Invalid input! Please enter an integer.")

    return numbers

# Get and display the filtered numbers
valid_numbers = collect_valid_numbers()
print("Filtered List:", valid_numbers)
