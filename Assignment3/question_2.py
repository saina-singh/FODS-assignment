'''
Python program to copy the contents of one file to another and display the output.
'''

def copy_file(source_file, destination_file):
    '''
    Function to copy contents from source_file to destination_file and print the output.
    '''
    try:
        with open(source_file, 'r', encoding='utf-8') as src:
            content = src.read()
        
        with open(destination_file, 'w', encoding='utf-8') as dest:
            dest.write(content)
        
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.\n")
        
        # Display the copied content
        print("Copied Content:\n")
        print(content)

    except FileNotFoundError:
        print(f"Error: '{source_file}' not found. Make sure the file exists.")

# Example usage
source = "source.txt"       # Ensure this file exists
destination = "destination.txt"
copy_file(source, destination)
