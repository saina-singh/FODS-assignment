'''
Python program to find and replace a specific word in a file and display the output.
'''

def find_and_replace(filename, old_word, new_word):
    '''
    Function to replace all occurrences of old_word with new_word in a file and print the updated content.
    '''
    try:
        # Read the file content
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Replace the word
        updated_content = content.replace(old_word, new_word)

        # Write the updated content back to the file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(updated_content)
        
        print(f"Replaced '{old_word}' with '{new_word}' in '{filename}' successfully!\n")

        # Display the updated content
        print("Updated File Content:\n")
        print(updated_content)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Example usage
filename = "sample2.txt"  # Replace with your actual file name
old_word = "Python"       # Word to be replaced
new_word = "Java"         # New word to replace with

find_and_replace(filename, old_word, new_word)
