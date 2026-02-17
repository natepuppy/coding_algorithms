# Dictionary is much more memory efficient because you only store 
# what you use, not an array of 26 pointers for every letter

# !!! Inserting just a 3 letter word will result in 4 total nodes

class TrieNode:
    def __init__(self, is_word=False):
        self.is_word = is_word
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        if node.is_word: return False

        node.is_word = True
        return True
    
    def starts_with(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True

    def search(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.is_word


trie = Trie()
trie.insert("apple")
trie.insert("app")
print(trie.search("apple"))
print(trie.search("apples"))
print(trie.starts_with("app"))
