# Updated for Python's 0-based indexing:
# leftChild of i  = heap[2 * i + 1]
# rightChild of i = heap[2 * i + 2]
# parent of i     = heap[(i - 1) // 2]


import heapq

# 1. Create a raw list
arr = [10, 5, 18, 2, 35, 1]

heapq.heapify(arr)
heapq.heappush(arr, 4)
smallest = heapq.heappop(arr)
print(f"Smallest currently is: {arr[0]}") # Should be 2

top_three = heapq.nlargest(3, arr)
print(top_three)  # Output: [35, 18, 10]
