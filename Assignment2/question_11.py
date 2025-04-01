'''
Dictionary operations: Concatenation, Addition, Update, Removal, Sum, Multiplication, Max & Min.
'''

# (a) Concatenating dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

nums = {**dic1, **dic2, **dic3}  # Merge dictionaries
print("Concatenated Dictionary:", nums)

# (b) Adding a new key/value pair (7, 70)
nums[7] = 70
print("After Adding (7, 70):", nums)

# (c) Updating value of key 3 to 80
nums[3] = 80
print("After Updating key 3 to 80:", nums)

# (d) Removing the third item (key 3 in this case)
nums.pop(3)
print("After Removing the third item (key 3):", nums)

# (e) Sum of all values in the dictionary
sum_values = sum(nums.values())
print("Sum of all values:", sum_values)

# (f) Multiplication of all values in the dictionary
product = 1
for value in nums.values():
    product *= value
print("Multiplication of all values:", product)

# (g) Maximum and Minimum values in nums
max_value = max(nums.values())
min_value = min(nums.values())

print("Maximum Value:", max_value)
print("Minimum Value:", min_value)
