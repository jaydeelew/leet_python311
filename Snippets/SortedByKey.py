# Example 1: Sorting a list of tuples by the second element
tuples = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print("Sorted by second element:", sorted_tuples)

# Example 2: Sorting a list of dictionaries by a specific key
dicts = [{"name": "John", "age": 25}, {"name": "Jane", "age": 22}, {"name": "Doe", "age": 30}]
sorted_dicts = sorted(dicts, key=lambda x: x["age"])
print("Sorted by age:", sorted_dicts)

# Example 3: Sorting a list of strings by their length
strings = ["apple", "banana", "cherry", "date"]
sorted_strings = sorted(strings, key=len)
print("Sorted by length:", sorted_strings)

# Example 4: Sorting a list of integers by their absolute value
numbers = [-5, 3, -2, 1, -4]
sorted_numbers = sorted(numbers, key=abs)
print("Sorted by absolute value:", sorted_numbers)
