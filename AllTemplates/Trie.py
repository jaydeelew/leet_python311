# Trie as in reTRIEval of words/data
class TrieNode:
    def __init__(self):
        # children is a dictionary where each key is a character in a word and the value is a TrieNode
        self.children = {}
        self.end_of_word = False

    # def all_suffixes(self):
    #     if self.end_of_word:
    #         yield ""
    #     for char, child in self.children.items():
    #         for suffix in child.all_suffixes():
    #             yield char + suffix

    def all_suffixes(self):
        suffix_list = []
        if self.end_of_word:
            # appending the empty string to the list of suffixes
            # begins the process of adding the current character to the beginning of each suffixe
            # since the second for loop below needs to iterate over something to begin building the final suffixe
            suffix_list.append("")
        for char, child in self.children.items():
            # iterate over the list of suffixes returned by the child
            # and add the current character to the beginning of each suffix
            for suffix in child.all_suffixes():
                suffix_list.append(char + suffix)
        return suffix_list


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
        return [prefix + suffixes for suffixes in curr.all_suffixes()]

    # def startswith(self, prefix):
    #     return True if self.locate(prefix) else False

    def remove(self, word):
        curr = self.locate(word)
        if curr:
            curr.end_of_word = False


t = Trie()

# arr = ["arm", "arms", "at", "be", "bet"]
arr = ["are", "arm"]
for w in arr:
    t.insert(w)

print(t.starts_with("a"))
