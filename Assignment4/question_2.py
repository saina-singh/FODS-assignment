''' write a program by asking user to input two numbers a, b and generate a random array of shape (a, b) 
and print the array and avg of the arrayimport numpy as np
'''
import numpy as np  # Import numpy

# Function to generate random array and calculate its average
def generate_random_array(a, b):
    # Generate a random array of shape (a, b)
    random_array = np.random.rand(a, b)
    
    # Calculate the average of the array
    average = np.mean(random_array)
    
    # Print the random array
    print("Random Array:")
    print(random_array)
    
    # Print the average of the array
    print("\nAverage of the array:", average)

# Input: Take two integers a and b as input from the user
a = int(input("Enter the number of rows (a): "))
b = int(input("Enter the number of columns (b): "))

# Call the function to generate the array and compute the average
generate_random_array(a, b)

