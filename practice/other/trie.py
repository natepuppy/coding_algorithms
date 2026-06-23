# Dictionary is much more memory efficient because you only store 
# what you use, not an array of 26 pointers for every letter

# !!! Inserting just a 3 letter word will result in 4 total nodes

class TrieNode:
    def __init__(self):
        self.children = {} # defaultdict??
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        node = self.root

        for char in s:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_word = True

    def search(self, s):
        node = self.root

        for char in s:
            if char not in node.children:
                return False

            node = node.children[char]
        
        return node.is_word

    def starts_with(self, s):
        node = self.root

        for char in s:
            if char not in node.children:
                return False

            node = node.children[char]
        
        return True































trie = Trie()
trie.insert("apple")
trie.insert("app")
print(trie.search("apple"))
print(trie.search("apples"))
print(trie.starts_with("app"))

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, s):
        node = self.root

        for char in s:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]
        
        node.is_end = True # Doing this outside loop is easier

    def search(self, s):
        node = self.root

        for char in s:
            if char not in node.children:
                return False

            node = node.children[char]

        return node.is_end # do this at the end!!!!!

    def starts_with(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False

            node = node.children[char]

        return True # NOTICE!! This is the only line that differs from search.
        

