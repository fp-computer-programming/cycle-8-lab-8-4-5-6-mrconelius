# Define the function is_palindrome that takes a string word as input
def is_palindrome(word):
    # Convert the input word to lowercase to make the comparison case-insensitive
    word = word.lower()
    
    # Use slicing to reverse the word
    reversed_word = word[::-1]
    
    # Check if the original word is the same as the reversed word
    if word == reversed_word:
        # Return True if it's a palindrome
        return True
    else:
        # Return False if it's not a palindrome
        return False

# Example usage:
# You can test the function with different words
word1 = "GTA6"
word2 = "python"
word3 = "level"
word4 = "fishing"

result1 = is_palindrome(word1)
result2 = is_palindrome(word2)
result3 = is_palindrome(word3)
result4 = is_palindrome(word4)

# Print the results
print(f"Is '{word1}' a palindrome? {result1}")
print(f"Is '{word2}' a palindrome? {result2}")
print(f"Is '{word3}' a palindrome? {result3}")
print(f"Is '{word4}' a palindrome? {result4}")
