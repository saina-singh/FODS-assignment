'''
Program to find the Euclidean distance between two points.
Formula: d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
'''

import math

# Taking coordinate inputs
x1, y1 = map(float, input("Enter first coordinate (x1 y1): ").split())
x2, y2 = map(float, input("Enter second coordinate (x2 y2): ").split())

# Calculating Euclidean distance
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"Euclidean distance: {distance:.2f}")
