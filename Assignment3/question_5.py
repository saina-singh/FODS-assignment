"""
Reads a file and counts the occurrence of each word.
"""
import string

def count_word_occurrences(filename):

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

        # Convert text to lowercase and remove punctuation
        text = text.lower().translate(str.maketrans('', '', string.punctuation))

        # Split text into words
        words = text.split()

        # Count word occurrences
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        # Display the word count
        print("\nWord Frequency in the File:\n")
        for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
            print(f"{word}: {count}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
filename = "sample3.txt"  # Replace with your actual file name
count_word_occurrences(filename)
