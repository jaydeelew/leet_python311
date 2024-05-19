# Trie as in reTRIEval of words/data
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

    def allRemainders(self):
        if self.end_of_word:
            yield ""
        for char, child in self.children.items():
            for remainder in child.allRemainders():
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
        return current and current.end_of_word

    def startsWith(self, prefix):
        current = self.locate(prefix)
        if not current:
            return []
        return [prefix + remainder for remainder in current.allRemainders()]

    # def startsWith(self, prefix):
    #     current = self.locate(prefix)
    #     return True if current else False

    def remove(self, word):
        current = self.root
        if self.search(word):
            for char in word:
                current = current.children[char]
            current.end_of_word = False


t = Trie()

arr = ["arm", "arms", "at", "be", "bet"]
for w in arr:
    t.insert(w)

print(t.startsWith("b"))
