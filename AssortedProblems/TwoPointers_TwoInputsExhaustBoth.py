# Two pointers: two inputs, exhaust both

# def fn(arr1, arr2):
#     i = j = ans = 0

#     while i < len(arr1) and j < len(arr2):
#         # do some logic here
#         if CONDITION:
#             i += 1
#         else:
#             j += 1

#     while i < len(arr1):
#         # do logic
#         i += 1

#     while j < len(arr2):
#         # do logic
#         j += 1

#     return ans


# Given two sorted integer arrays, return an array that combines both of them and is also sorted.
def combine(arr1, arr2):
    sorted_arr = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1

    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1

    return sorted_arr


arr1 = [1, 4, 7, 20]
arr2 = [3, 5, 6]
# Output: [1, 3, 4, 5, 6, 7, 20]

print(combine(arr1, arr2))
