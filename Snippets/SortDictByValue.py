# How to sort a Python dict by value

my_dict = {"a": 4, "b": 3, "c": 2, "d": 1}
sorted_by_value = sorted(my_dict.items(), key=lambda x: x[1])

print(sorted_by_value)
# Output: [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
