from collections import Counter


def maxNumberOfBalloons(text):
    balloon = "balloon"
    counts = Counter(text)

    if any(c not in counts for c in balloon):
        return 0
    else:
        return min(counts["b"], counts["a"], counts["l"] // 2, counts["o"] // 2, counts["n"])


str = "nlaebolko"
print(maxNumberOfBalloons(str))
