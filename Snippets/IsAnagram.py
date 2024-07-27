from collections import Counter


# Solution 1: Sorting
# Time complexity: O(n log n)
# Space complexity: O(n)
def isAnagram(s, t):
    return sorted(s) == sorted(t)


# Solution 2: Counter
# Time complexity: O(n)
# Space complexity: O(n)
def isAnagram2(s, t):
    return Counter(s) == Counter(t)


print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))
print(isAnagram2("anagram", "nagaram"))
print(isAnagram2("rat", "car"))
