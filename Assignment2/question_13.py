'''
Function to find common letters between two words.
'''
def word_intersection():
    word1 = input("Enter the first word: ").lower()  # Convert to lowercase for consistency
    word2 = input("Enter the second word: ").lower()

    common_letters = set(word1) & set(word2)  # Find common letters using set intersection

    if common_letters:
        print("Common letters:", "".join(sorted(common_letters)))  # Sort for readability
    else:
        print("No common letters found.")

# Call the function
word_intersection()
