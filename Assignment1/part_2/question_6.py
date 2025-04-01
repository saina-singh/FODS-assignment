'''
Program to find numbers between 1500 and 2000 that are divisible by 7 and multiple of 5.
'''

# Finding numbers in the range
result = [num for num in range(1500, 2001) if num % 7 == 0 and num % 5 == 0]

# Printing the results
print("Numbers divisible by 7 and multiple of 5:", result)

#Output: (1505, 1540, 1575, 1610, 1645, 1680, 1715, 1750, 1785, 1820, 1855, 1890, 1925, 1960, 1995)