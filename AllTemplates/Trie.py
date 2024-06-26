# Trie as in reTRIEval of words/data
class TrieNode:
    def __init__(self):
        # children is a dictionary of TrieNodes where each key is a character and the value is the TrieNode
        self.children = {}
        self.end_of_word = False

    def all_remainders(self):
        if self.end_of_word:
            print("end")
            yield ""
        for char, child in self.children.items():
            for remainder in child.all_remainders():
                print(char + remainder)
                yield char + remainder


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end_of_word = True

    def locate(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return None
            curr = curr.children[char]
        return curr

    def search(self, word):
        curr = self.locate(word)
        # If curr is None (meaning the word is not even partially in the Trie),
        # trying to access curr.end_of_word would result in an AttributeError.
        # This is because you would be trying to access an attribute of a None object.
        # Checking curr and curr.end_of_word ensures that you only check
        # curr.end_of_word if curr is not None, thus avoiding potential errors
        return curr and curr.end_of_word

    def starts_with(self, prefix):
        curr = self.locate(prefix)
        if not curr:
            return []
        return [prefix + remainder for remainder in curr.all_remainders()]

    # def startswith(self, prefix):
    #     return True if self.locate(prefix) else False

    def remove(self, word):
        curr = self.locate(word)
        if curr:
            curr.end_of_word = False


t = Trie()

arr = ["arm", "arms", "at", "be", "bet"]
for w in arr:
    t.insert(w)

print(t.starts_with("a"))
