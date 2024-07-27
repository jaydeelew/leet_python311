# Examples of string slicing

# Define a sample string
sample_string = "Hello, World!"

# Slicing to get the first 5 characters
first_five = sample_string[:5]
print(f"First five characters: {first_five}")

# Slicing to get the last 6 characters
last_six = sample_string[-6:]
print(f"Last six characters: {last_six}")

# Slicing to get characters from index 7 to 11
middle_slice = sample_string[7:12]
print(f"Characters from index 7 to 11: {middle_slice}")

# Slicing to get every second character
every_second_char = sample_string[::2]
print(f"Every second character: {every_second_char}")

# Slicing to get the string in reverse
reversed_string = sample_string[::-1]
print(f"Reversed string: {reversed_string}")

# Slicing to get a substring from index 2 to the second last character
substring = sample_string[2:-1]
print(f"Substring from index 2 to the second last character: {substring}")
