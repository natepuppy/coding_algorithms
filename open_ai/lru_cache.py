# https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # Map key to Node
        
        # Dummy nodes to avoid null checks
        self.start = Node(0, 0) # Least Recently Used (LRU) side
        self.end = Node(0, 0)   # Most Recently Used (MRU) side
        
        self.start.next = self.end
        self.end.prev = self.start

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node) # Move to the MRU side (end)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        # Always create/update node and move to MRU side
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        # Evict if over capacity
        if len(self.cache) > self.capacity:
            lru_node = self.start.next
            self.remove(lru_node)
            del self.cache[lru_node.key]

    # Helper: Always adds to the MRU side (right before 'end')
    def insert(self, node) -> None:
        previous = self.end.prev
        previous.next = node
        node.prev = previous
        node.next = self.end
        self.end.prev = node
    
    # Helper: Standard DLL removal
    def remove(self, node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev