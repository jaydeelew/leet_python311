class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

    # this function in node class since need to enter into current node:
    def allWords(self):
        if self.end_of_word:
            yield ""
        for char, child in self.children.items():
            for word in child.allWords():
                yield char + word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
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
        return [prefix + rest for rest in current.allWords()]

    # def startsWith(self, prefix):
    #     current = self.locate(prefix)
    #     return True if current else False

    def remove(self, word):
        current = self.root
        if self.search(word):
            for char in word:
                current = current.children[char]
            current.end_of_word = False

    # def startsWith(self, prefix):
    #     current = self.locate(prefix)
    #     if current is None:
    #         return []

    #     def build(current):
    #         if current.end_of_word:
    #             nonlocal word
    #             ans.append("".join(word))
    #         for char, child_node in current.children.items():
    #             word.append(char)
    #             build(child_node)

    #         word.pop()

    #     ans = []
    #     word = []
    #     for c in prefix:
    #         word.append(c)

    #     build(current)
    #     return ans


t = Trie()

arr = ["arm", "arms", "at", "be", "bet"]
for w in arr:
    t.insert(w)

print(t.startsWith("ar"))
