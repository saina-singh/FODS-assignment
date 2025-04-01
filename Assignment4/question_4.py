'''
To create a identity matrix of shape (3,4) with code for it
'''
import numpy as np  # Importing numpy library

# Function to create a "modified" identity matrix with shape (3, 4)
def create_identity_matrix():
    # Create a zero matrix of shape (3, 4)
    identity_matrix = np.zeros((3, 4))
    
    # Fill the diagonal with 1's up to the smallest dimension (3 in this case)
    np.fill_diagonal(identity_matrix, 1)
    
    # Print the resulting matrix
    print("Identity Matrix (3x4):")
    print(identity_matrix)

# Call the function to create and print the matrix
create_identity_matrix()
