'''
To create an array of random integer numbers as a numpy array, sort them and perform operations such as reshaping
of the array into matrix of feasible dimensions. 
'''
import numpy as np  # Importing numpy library

# Function to generate random array, sort it, and reshape it into a matrix
def reshape_array():
    # Step 1: Create a random array of integers (1 row, 10 columns)
    random_array = np.random.randint(1, 100, 10)  # 10 random integers between 1 and 100
    
    # Print the original random array
    print("Original Random Array:")
    print(random_array)
    
    # Step 2: Sort the array in ascending order
    sorted_array = np.sort(random_array)
    
    # Print the sorted array
    print("\nSorted Array:")
    print(sorted_array)
    
    # Step 3: Reshape the array into a matrix of feasible dimensions
    # Reshaping into 2x5 matrix (since 1 * 10 can be reshaped into 2 * 5)
    reshaped_matrix = sorted_array.reshape(2, 5)
    
    # Print the reshaped matrix
    print("\nReshaped Matrix (2x5):")
    print(reshaped_matrix)
    
    # Step 4: Reshaping into 5x2 matrix (valid for 1 * 10 as well)
    reshaped_matrix_2 = sorted_array.reshape(5, 2)
    
    # Print the reshaped matrix 5x2
    print("\nReshaped Matrix (5x2):")
    print(reshaped_matrix_2)

# Call the function to execute the operations
reshape_array()
