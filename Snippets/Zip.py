# Example 1: Basic usage of zip
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
zipped = zip(list1, list2)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# Example 2: Using zip with different lengths
list1 = [1, 2, 3, 4]
list2 = ["a", "b", "c"]
zipped = zip(list1, list2)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# Example 3: Unzipping a zipped object
zipped = zip([1, 2, 3], ["a", "b", "c"])
list1, list2 = zip(*zipped)
print(list1)  # Output: (1, 2, 3)
print(list2)  # Output: ('a', 'b', 'c')

# Example 4: Using zip with three lists
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
list3 = [True, False, True]
zipped = zip(list1, list2, list3)
print(list(zipped))  # Output: [(1, 'a', True), (2, 'b', False), (3, 'c', True)]

# Example 5: Using zip with a dictionary
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]
zipped = zip(keys, values)
dictionary = dict(zipped)
print(dictionary)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
