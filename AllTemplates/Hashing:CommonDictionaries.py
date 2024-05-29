from collections import defaultdict, Counter


# regular dictionary
def count_occurrences(arr):
    occurrence_map = {}
    for num in arr:
        if num in occurrence_map:
            occurrence_map[num] += 1
        else:
            occurrence_map[num] = 1
    return occurrence_map


# defaultdict
def count_occurrences2(arr):
    occurrence_map = defaultdict(int)
    for num in arr:
        occurrence_map[num] += 1
    return occurrence_map


# Counter
def count_occurrences3(arr):
    occurrence_map = Counter(arr)
    return occurrence_map


# Test case
test_array = [1, 2, 2, 3, 3, 3]
print(count_occurrences(test_array))  # Expected output: {1: 1, 2: 2, 3: 3}
print(count_occurrences2(test_array))  # Expected output: {1: 1, 2: 2, 3: 3}
print(count_occurrences3(test_array))  # Expected output: {1: 1, 2: 2, 3: 3}
