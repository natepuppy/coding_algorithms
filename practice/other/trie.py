class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        # Code will be implemented here
        pass

    def search(self, word):
        # Code will be implemented here
        pass

    def startsWith(self, prefix):
        # Code will be implemented here
        pass


trie = Trie()
trie.insert("apple")
trie.insert("app")
print(trie.search("apple"))
print(trie.search("apples"))
print(trie.startsWith("app"))
