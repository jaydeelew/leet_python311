# 1832. Check if the Sentence Is Pangram
# A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.


def checkIfPangram(sentence: str) -> bool:
    seen = set(sentence)
    return True if len(seen) == 26 else False


sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: True

print(checkIfPangram(sentence))
