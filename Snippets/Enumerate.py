# Example 1: Basic usage of enumerate
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Example 2: Using enumerate with a custom start index
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# Example 3: Enumerate with a list of tuples
students = [("John", "A"), ("Jane", "B"), ("Doe", "C")]
for index, (name, grade) in enumerate(students):
    print(index, name, grade)

# Example 4: Enumerate with a dictionary
grades = {"John": "A", "Jane": "B", "Doe": "C"}
for index, (name, grade) in enumerate(grades.items()):
    print(index, name, grade)

# Example 5: Enumerate with a string
word = "hello"
for index, letter in enumerate(word, 1):  # start enumerating at !
    print(f"{index}: {letter}")
