# Trie as in reTRIEval of words/data
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

    def all_remainders(self):
        if self.end_of_word:
            yield ""
        for char, child in self.children.items():
            for remainder in child.all_remainders():
                yield char + remainder


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                # children is a dictionary of TrieNodes where each key is a character and the value is the TrieNode
                # we do not need a defaultdict here since by creating the TrieNode we automatically create the key
                current.children[char] = TrieNode()
            current = current.children[char]
        current.end_of_word = True

    def locate(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return
            current = current.children[char]
        return current

    def search(self, word):
        current = self.locate(word)
        # If current is None (meaning the word is not even partially in the Trie),
        # trying to access current.end_of_word would result in an AttributeError.
        # This is because you would be trying to access an attribute of a None object.
        # Checking current and current.end_of_word ensures that you only check
        # current.end_of_word if current is not None, thus avoiding potential errors
        return current and current.end_of_word

    def starts_with(self, prefix):
        current = self.locate(prefix)
        if not current:
            return []
        return [prefix + remainder for remainder in current.all_remainders()]

    # def starts_with(self, prefix):
    #     current = self.locate(prefix)
    #     return True if current else False

    def remove(self, word):
        current = self.locate(word)
        if current:
            current.end_of_word = False


t = Trie()

arr = ["arm", "arms", "at", "be", "bet"]
for w in arr:
    t.insert(w)

print(t.starts_with("a"))
