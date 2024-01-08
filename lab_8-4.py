# Define the function count_a that takes a string word as input
def count_a(word):
    # Initialize a variable to store the count of 'a' characters
    a_count = 0
    
    # Iterate through each character in the word
    for char in word:
        # Check if the character is either 'a' or 'A'
        if char == 'a' or char == 'A':
            # Increment the count if it's 'a' or 'A'
            a_count += 1
    
    # Return the final count of 'a' characters
    return a_count

# Example usage:
# You can test the function with different words
word1 = "orange"
word2 = "cranberry"
word3 = "programming"
word4 = "tree"
result1 = count_a(word1)
result2 = count_a(word2)
result3 = count_a(word3)
result4 = count_a(word4)

# Print the results
print(f"Number of 'a' characters in '{word1}': {result1}")
print(f"Number of 'a' characters in '{word2}': {result2}")
print(f"Number of 'a' characters in '{word3}': {result3}")
print(f"Number of 'a' characters in '{word4}': {result4}")
