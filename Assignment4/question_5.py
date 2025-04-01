'''
 To create a 5x5 matrix with values ranging from 0 to 4
'''
import numpy as np  # Importing numpy library

# Function to create a 5x5 matrix with values ranging from 0 to 4 in each row
def create_matrix():
    # Create a matrix where each row is a range from 0 to 4
    matrix = np.array([np.arange(5) for _ in range(5)])
    
    # Print the resulting matrix
    print("5x5 Matrix with values ranging from 0 to 4 in each row:")
    print(matrix)

# Call the function to create and print the matrix
create_matrix()

