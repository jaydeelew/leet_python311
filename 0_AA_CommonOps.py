import random
import re
import math
import string
from collections import Counter
from time import sleep
from itertools import groupby

# Reverse a list in place
original_list = [1, 2, 3, 4, 5]
original_list.reverse()
print("List reversed in place:", original_list)

# Reverse a list by creating a new list
lst = [1, 2, 3, 4, 5]
print("List reversed with with slicing:", lst[::-1])

# Merge two sorted lists into one of the lists in O(n + m) time
list1 = [1, 3, 5, 7, 11]
list2 = [4, 6, 11, 12]
list1.extend(list2)
print("Merged sorted lists:", list1)

# Count the occurrences of an element in a list
numbers = [1, 2, 2, 3, 2, 4, 5]
print("Count of 2 in the list:", numbers.count(2))

# Remove duplicates from a list
duplicates = [1, 2, 2, 3, 3, 4, 5, 5]
print("List with duplicates removed:", list(set(duplicates)))

# Find the common elements between two lists
list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6]
print("Common elements between lists:", list(set(list_a) & set(list_b)))

# Find the union of elements between two lists
list_x = [1, 2, 3]
list_y = [3, 4, 5]
print("Union of elements between lists:", list(set(list_x) | (set(list_y))))

# Sort a list of dictionaries by a key
list_dict = [{"name": "Bob", "age": 25}, {"name": "Tom", "age": 19}, {"name": "Alice", "age": 22}]
print("List of dictionaries sorted by age:", sorted(list_dict, key=lambda x: x["age"]))

# Flatten a nested list
nested = [[1, 2], [3, 4], [5, 6]]
print("Flattened nested list:", [item for sublist in nested for item in sublist])

# Generate a list of even numbers in range: 0 to 10
print("Even numbers from 0 to 10:", [num for num in range(11) if num % 2 == 0])

# Create a list of 5 random numbers between 1 and 100
print("5 random numbers between 1 and 100:", [random.randint(1, 100) for _ in range(5)])

# Find the product of all elements in a list
numbers = [1, 2, 3, 4]
print("Product of all elements:", math.prod(numbers))

# Concatenate two lists
list1 = [1, 2]
list2 = [3, 4]
print("Concatenated lists:", list1 + list2)

# Generate a list of squares in range: 0 to 4
print("Squares from 0 to 4:", [x**2 for x in range(5)])

# Filter even and odd numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
print("Even numbers in list:", [x for x in numbers if x % 2 == 0])
print("Odd numbers in list:", [x for x in numbers if x % 2 != 0])

# Find the index of an element in a list
items = ["apple", "banana", "orange"]
print("Index of 'banana':", items.index("banana"))

# Remove an element from a list by value
fruits = ["apple", "banana", "orange"]
fruits.remove("banana")
print("List after removing 'banana':", fruits)

# Insert an element at a specific position in a list
numbers = [1, 2, 4]
pos = 2
element = 3
print("List after inserting element:", numbers.insert(pos, element))

# Rotate a list left and right by 2
numbers = [1, 2, 3, 4, 5]
rotations = 2
# A left rotation is the same as removing the first rotations elements and adding them to the end.
print("List rotated left by 2:", numbers[rotations:] + numbers[:rotations])
# A right rotation is the same as removing the last rotations elements and adding them to the beginning.
print("List rotated right by 2:", numbers[-rotations:] + numbers[:-rotations])

# Check if all elements in a list are unique
numbers = [1, 5, 2, 3, 4, 5]
print("All elements are unique:", len(numbers) == len(set(numbers)))

# Create a dictionary from two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
print("Dictionary from two lists:", dict(zip(keys, values)))

# Swap keys and values in a dictionary
original = {"a": 1, "b": 2, "c": 3}
print("Dictionary with swapped keys and values:", {v: k for k, v in original.items()})

# Merge two dictionaries with the second dictionary overwriting the values of the first
# if there are dubplicate keys
dict1 = {"a": 1, "b": 2, "c": 5}
dict2 = {"c": 3, "d": 4}
print("Merged dictionaries:", dict1 | dict2)

# Find the intersection of two dictionaries while retaining all the values in any duplicated keys
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "c": 30, "d": 40}
print({key: (dict1[key], dict2[key]) for key in dict1 if key in dict2})
# Output: {'b': (2, 20), 'c': (3, 30)}

# Remove a key from a dictionary
data = {"a": 1, "b": 2, "c": 3}
data.pop("b")
print("Dictionary after removing key 'b':", data)

# Check if a key exists in a dictionary
data = {"name": "John", "age": 30}
print("Does key 'age' exist in dictionary?:", "age" in data)

# Find the maximum and minimum values in a dictionary
scores = {"John": 85, "Alice": 92, "Bob": 78}
print("Maximum value in dictionary:", max(scores.values()))
print("Minimum value in dictionary:", min(scores.values()))

# Sort by values first, then keys
data = {"b": 2, "a": 2, "c": 1, "d": 1}
print(sorted(data.items(), key=lambda x: (x[1], x[0])))

# Count the occurrences of characters in a string
text = "hello"
print("Character frequency in string:", dict(Counter(text)))

# Reverse a string
text = "hello"
print("Reversed string:", text[::-1])

# Check if a string is a palindrome
text = "radar"
print("Is string a palindrome?:", text[::-1] == text)

# Replace a substring in a string
text = "Hello World"
print("String after replacing 'World' with 'Python':", text.replace("World", "Python"))

# Remove whitespace from a string
text = "  Hello  World  "
print("String with whitespace removed:", text.strip())

# Split a string into a list of words
text = "Hello World of Python"
print("String split into words:", text.split())

# Join a list of words into a string
words = ["Hello", "World"]
print("Words joined into string:", " ".join(words))

# Convert a string to uppercase and lowercase
text = "Hello"
print("String in uppercase:", text.upper())
print("String in lowercase:", text.lower())

# Find the first non-repeating character anywhere in a string
s = "ababcd"
counts = Counter(s)
print("First non-repeating character:", next((ch for ch in s if counts[ch] == 1), None))

# Find the first non-repeating (consecutively) character in a string
text = "lleettcodde"
for char, group in groupby(text):
    if len(list(group)) == 1:
        print("First non-repeating character:", char)
        break

# Check if a string contains a substring
text = "Hello World"
print("Does text contain 'or'?: ", "or" in text)

# Count vowels and consonants in a string
text = "Hello"
vowels = set("aeiouAEIOU")
print("Number of vowels:", sum(1 for char in text if char.isalpha() and char in vowels))
print("Number of consonants:", sum(1 for char in text if char.isalpha() and char not in vowels))

# Generate a random string of 5 letters
print("Random 5-letter string:", "".join(random.choices(string.ascii_letters, k=5)))

# Check if a string starts or ends with a substring
text = "Hello World"
print("Does string start with 'Hello'?:", text.startswith("Hello"))
print("Does string end with 'Hello'?:", text.endswith("Hello"))

# Find the frequency of words in a string
text = "hello world hello python"
lst = text.split()
print("Word frequency in string:", Counter(lst))

# Extract numbers from a string
text = "abc123def456"
print("Numbers extracted (using list comprehension):", [x for x in text if x.isdecimal()])
# Output: ['1', '2', '3', '4', '5', '6']
print("Numbers extracted (using filter):", "".join(filter(lambda x: x.isdecimal(), text)))
# Output: 123456
print("Numbers extracted (using regex):", re.findall(r"\d+", text))
# Output: ['123', '456']

# Check if a string contains only digits
text = "12345"
print("Is string only digits?:", text.isdigit())

# Add and remove elements in a set
numbers = {1, 2, 3}
numbers.add(4)
numbers.remove(2)
print("Set after adding 4 and removing 2:", numbers)

# Find the union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union of sets:", set1 | set2)

# Find the intersection of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Intersection of sets:", set1 & set2)

# Find the difference between two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Difference between sets:", set1 - set2)


# Given a list of keyword arguments to a function, have the function print one of the keyword arguments
# a="alpha", b="beta", c="delta"
def key_word_args(**kwargs):
    # for keyword, value in kwargs.items():
    #     print("The value of keyword", keyword, "is", value)
    print(kwargs["c"])


key_word_args(a="alpha", b="beta", c="delta")


# Given a list of positional arguments to a function, have the function print the second argument
# "alpha", "beta", "delta"
def args(*args):
    # for value in args:
    #     print("The arg is", value)
    print(args[1])


args("alpha", "beta", "delta")

# Build a string from a list of characters
arr = ["h", "e", "l", "l", "o"]
print("".join(arr))

# Split a string up into separate characters in an array
str = "hello"
print(list(str))

# Format a number with commas
print(f"{10000000000:,}")

# Cycle through "Loading .", "Loading ..", "Loading ..." on the same line in one second intervals
# from time import sleep
while True:
    for i in range(0, 4):
        print("Loading" + "." * i, end="\r")
        sleep(1)
    print(" " * 20, end="\r")
