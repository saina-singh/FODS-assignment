'''
Python program to count the number of lines, words, and characters in a text file.
'''

def count_file_contents(filename):
    '''
    Function to count lines, words, and characters in a given file.
    '''
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_chars = sum(len(line) for line in lines)

        print(f"Lines: {num_lines}")
        print(f"Words: {num_words}")
        print(f"Characters: {num_chars}")

    except FileNotFoundError:
        print("Error: File not found.")

# Example usage
filename = "sample.txt"  # Replace with the actual file name
count_file_contents(filename)
