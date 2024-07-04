def shorter_than_three(string):
    return len(string) < 3


strings = ["today", "me", "for", "mouthful", "be", "tart", "a"]

# filtered = filter(lambda x: len(x) < 3, strings)
filtered = filter(shorter_than_three, strings)

print(list(filtered))
