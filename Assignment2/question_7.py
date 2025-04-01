'''
Program to accept a list of names and count occurrences of the letter 'a'.
'''

# Function to collect names and count 'a' occurrences
def count_a_in_names():
    names = []
    total_a_count = 0

    while True:
        name = input("Enter a name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break  # Exit the loop if user types 'done'
        
        names.append(name)  # Add name to the list
        total_a_count += name.lower().count('a')  # Count 'a' in the name

    return names, total_a_count

# Get names and count 'a'
names_list, a_count = count_a_in_names()

# Display results
print("Names List:", names_list)
print("Total occurrences of 'a':", a_count)
