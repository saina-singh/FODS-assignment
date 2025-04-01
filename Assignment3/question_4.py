'''
Python program to read a CSV file and display its contents in a tabular format.
'''

import csv
from tabulate import tabulate  # Install using: pip install tabulate

def read_csv_and_display(filename):
    '''
    Function to read a CSV file and display its contents in a table.
    '''
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)  # Convert to a list

            if not data:
                print("The CSV file is empty.")
                return

            # Display the CSV contents as a table
            print("\nCSV File Contents:\n")
            print(tabulate(data, headers="firstrow", tablefmt="grid"))

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Example usage
filename = "data.csv"  # Replace with the actual CSV filename
read_csv_and_display(filename)
