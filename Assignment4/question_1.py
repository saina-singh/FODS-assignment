"""
Create a null vector of size 10 but the fifth value is 1
"""
import numpy as np

# Create a null vector of size 10
vector = np.zeros(10)
vector[4] = 1  # Set the fifth value to 1

print("Null vector with fifth value as 1:\n", vector)

#Expected Output:(0. 0. 0. 0. 1. 0. 0. 0. 0. 0.)