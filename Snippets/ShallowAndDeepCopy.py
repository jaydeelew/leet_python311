import copy


def shallow_copy(original):
    shallow = original.copy()
    return shallow


def deep_copy(original):
    deep = copy.deepcopy(original)
    return deep


def slice_same_object(original):
    shallow = original[:]
    return (shallow, True) if shallow is original else (shallow, False)


def slice_diff_object(original):
    shallow = original[::-1]
    return (shallow, True) if shallow is original else (shallow, False)


# Test case for list of integers
print("Test case 1: List of integers")
original_list = [1, 2, 3, 4, 5]
shallow_list = shallow_copy(original_list)
deep_list = deep_copy(original_list)

print("Original:", original_list)
print("Shallow copy:", shallow_list)
print("Deep copy:", deep_list)

original_list[0] = 99
print("\nAfter modifying original:")
print("Original:", original_list)
print("Shallow copy:", shallow_list)
print("Deep copy:", deep_list)

# Test case for nested list
print("\nTest case 2: Nested list")
original_nested = [[1, 2], [3, 4]]
shallow_nested = shallow_copy(original_nested)
deep_nested = deep_copy(original_nested)

print("Original:", original_nested)
print("Shallow copy:", shallow_nested)
print("Deep copy:", deep_nested)

# shallow copy is affected since this list is made up of references to the original list elements
original_nested[0][0] = 99
print("\nAfter modifying original:")
print("Original:", original_nested)
print("Shallow copy:", shallow_nested)
print("Deep copy:", deep_nested)

# Test case for dictionary
print("\nTest case 3: Dictionary")
original_dict = {"a": [1, 2], "b": [3, 4]}
shallow_dict = shallow_copy(original_dict)
deep_dict = deep_copy(original_dict)

print("Original:", original_dict)
print("Shallow copy:", shallow_dict)
print("Deep copy:", deep_dict)

original_dict["a"][0] = 99
print("\nAfter modifying original:")
print("Original:", original_dict)
print("Shallow copy:", shallow_dict)
print("Deep copy:", deep_dict)

# Test case for shallow copy slice on string
# If string is unchanged, shallow copy is the same object
# If string is changed, shallow copy is a new object
original_string = "Hello, World!"
same_string, is_same_string = slice_same_object(original_string)
diff_string, is_diff_string = slice_diff_object(original_string)

print(f"\nOriginal: {original_string}")
print(f"{same_string}: Is same object: {is_same_string}")
print(f"{diff_string}: Is same object: {is_diff_string}")

# Test case for shallow copy slice on list
# If list is unchanged, shallow copy is new object
# If list is changed, shallow copy is a new object
original_list = [1, 2, 3, 4, 5]
same_list, is_same_list = slice_same_object(original_list)
diff_list, is_diff_list = slice_diff_object(original_list)

print(f"\nOriginal: {original_list}")
print(f"{same_list}: Is same object: {is_same_list}")
print(f"{diff_list}: Is same object: {is_diff_list}")
