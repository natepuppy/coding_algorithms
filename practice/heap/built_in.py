# Updated for Python's 0-based indexing:
# leftChild of i  = heap[2 * i + 1]
# rightChild of i = heap[2 * i + 2]
# parent of i     = heap[(i - 1) // 2]

import heapq

arr = [2,3,6,3,1,4,3,4,2]

heapq.heapify(arr)

print(arr)

heapq.heappush(arr, 7)

heapq.heappop(arr, 7)

result = heapq.nsmallest(3, arr)



print(result)
print(result[-1])
print("------")

while arr:
    el = heapq.heappop(arr)
    print(el)

