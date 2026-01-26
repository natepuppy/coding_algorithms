# leftChild of i = heap[2 * i]
# rightChild of i = heap[(2 * i) + 1] 
# parent of i = heap[i // 2]


import heapq

# 1. Create a raw list
data = [10, 5, 18, 2, 35, 1]

# 2. HEAPIFY: Transform list into a heap in-place
# This is O(n) complexity—much faster than inserting one by one.
heapq.heapify(data)
print(f"Heapified list: {data}") 
# Note: The list looks "unsorted" but follows the heap property: 
# data[i] <= data[2*i + 1] and data[i] <= data[2*i + 2]

# 3. PUSH: Add a new element
heapq.heappush(data, 4)
print(f"After pushing 4: {data}")

# 4. POP: Remove and return the smallest element
smallest = heapq.heappop(data)
print(f"Popped smallest: {smallest}")
print(f"Heap after pop: {data}")

# 5. PEEK: See the smallest without removing it
print(f"Smallest currently is: {data[0]}")





