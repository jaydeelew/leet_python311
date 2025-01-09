# 0. Combine Sorted Arrays
# Given two sorted integer arrays, return an array that combines both of them and is also sorted.


def combine(arr1, arr2):
    ans = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        # append to end of answer array the lesser of the two arrays at current i & j positions
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1
    # while there remains elements to add in either array, add them to answer array in order
    while i < len(arr1):
        ans.append(arr1[i])
        i += 1

    while j < len(arr2):
        ans.append(arr2[j])
        j += 1

    return ans


arr1 = [1, 4, 7, 20]
arr2 = [3, 5, 6]
# Output: [1, 3, 4, 5, 6, 7, 20]

print(combine(arr1, arr2))
