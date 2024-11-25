# Given an array of unsorted scores and the highest possible score, sort the scores.


def sort_scores(unsorted_scores, highest_possible_score):
    score_is_index = [0] * (highest_possible_score + 1)
    sorted_scores = []

    for score in unsorted_scores:
        score_is_index[score] += 1

    for i in range(highest_possible_score, -1, -1):
        if score_is_index[i] >= 1:
            for _ in range(score_is_index[i]):
                sorted_scores.append(i)

    return sorted_scores


# Time Complexity: O(N+M), where N and M are the size of inputArray[] and countArray[] respectively.
# Space Complexity: O(N+M), where N and M are the space taken by outputArray[] and countArray[] respectively.

# Advantage of Counting Sort:
# Counting sort generally performs faster than all comparison-based sorting algorithms, such as merge sort and quicksort, if the range of input is of the order of the number of input.
# Counting sort is easy to code
# Counting sort is a stable algorithm.

# Disadvantage of Counting Sort:
# Counting sort doesn’t work on decimal values.
# Counting sort is inefficient if the range of values to be sorted is very large.
# Counting sort is not an In-place sorting algorithm, It uses extra space for sorting the array elements.

unsorted_scores = [37, 89, 41, 65, 91, 53]
highest_possible_score = 100

print(sort_scores(unsorted_scores, highest_possible_score))

# Returns [91, 89, 65, 53, 41, 37]
