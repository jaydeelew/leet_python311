# Example 1: Create a list of squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print(f"Squares of numbers from 0 to 9: {squares}")

# Example 2: Create a list of even numbers from 0 to 19
evens = [x for x in range(20) if x % 2 == 0]
print(f"Even numbers from 0 to 19: {evens}")

# Example 3: Create a list of characters from a string
sample_string = "Hello, World!"
chars = [char for char in sample_string]
print(f"Characters in the string: {chars}")

# Example 4: Create a list of tuples (number, square) for numbers from 0 to 9
number_square_tuples = [(x, x**2) for x in range(10)]
print(f"Tuples of numbers and their squares: {number_square_tuples}")

# Example 5: Flatten a list of lists
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [item for sublist in list_of_lists for item in sublist]
print(f"Flattened list: {flattened_list}")

# Example 6: Create a list of uppercase characters from a string
uppercase_chars = [char.upper() for char in sample_string]
print(f"Uppercase characters in the string: {uppercase_chars}")

# Example 7: Create a list of lengths of words in a sentence
sentence = "The quick brown fox jumps over the lazy dog"
word_lengths = [len(word) for word in sentence.split()]
print(f"Lengths of words in the sentence: {word_lengths}")
