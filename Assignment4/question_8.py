'''
Pandas program to add, subtract, multiple and divide two Pandas Series
'''
import pandas as pd  # Importing pandas library

# Function to perform arithmetic operations on two Pandas Series
def perform_operations():
    # Step 1: Create two Pandas Series
    series1 = pd.Series([10, 20, 30, 40, 50])
    series2 = pd.Series([5, 15, 25, 35, 45])
    
    # Step 2: Perform arithmetic operations between the two Series
    
    # Addition
    addition_result = series1 + series2
    print("Addition of Series:")
    print(addition_result)
    
    # Subtraction
    subtraction_result = series1 - series2
    print("\nSubtraction of Series:")
    print(subtraction_result)
    
    # Multiplication
    multiplication_result = series1 * series2
    print("\nMultiplication of Series:")
    print(multiplication_result)
    
    # Division
    division_result = series1 / series2
    print("\nDivision of Series:")
    print(division_result)

# Call the function to execute the operations
perform_operations()
