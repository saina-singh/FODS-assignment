'''
A program to input an array of numbers from the user (at least 10 elements in list), sort them and 
perform slicing operations to get elements between indexes such as 2-5, 5-8, 2-9. 
'''
# Function to input array, sort it, and perform slicing operations
def array_operations():
    # Input: Take at least 10 numbers from the user
    input_array = input("Enter at least 10 numbers separated by spaces: ")
    
    # Convert the input string into a list of numbers (integers)
    num_list = list(map(int, input_array.split()))
    
    # Ensure there are at least 10 numbers in the list
    if len(num_list) < 10:
        print("Error: You must input at least 10 numbers.")
        return
    
    # Sort the array in ascending order
    num_list.sort()
    
    # Print the sorted array
    print("Sorted Array:", num_list)
    
    # Perform slicing operations:
    
    # Slice from index 2 to 5 (exclusive of 5)
    slice_2_5 = num_list[2:5]
    print("\nElements between index 2 and 5:", slice_2_5)
    
    # Slice from index 5 to 8 (exclusive of 8)
    slice_5_8 = num_list[5:8]
    print("Elements between index 5 and 8:", slice_5_8)
    
    # Slice from index 2 to 9 (exclusive of 9)
    slice_2_9 = num_list[2:9]
    print("Elements between index 2 and 9:", slice_2_9)

# Call the function to execute the operations
array_operations()
