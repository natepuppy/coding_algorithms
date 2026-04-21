# Dictionary is much more memory efficient because you only store 
# what you use, not an array of 26 pointers for every letter

# !!! Inserting just a 3 letter word will result in 4 total nodes




trie = Trie()
trie.insert("apple")
trie.insert("app")
print(trie.search("apple"))
print(trie.search("apples"))
print(trie.starts_with("app"))
