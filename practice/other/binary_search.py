arr = [1, 3, 5, 7, 7, 7, 9, 11]
target = 7

import bisect

# This results in 6 - Not 5!!!! Which is the first index that this element could be inserted at
result_id = bisect.bisect_right(arr, target) # Note: arr, target - NOT (target, arr)
print(result_id)

# Also results in 6
result_id = bisect.bisect_left(arr, 8)
print(result_id)

# Results in 3
result_id = bisect.bisect_left(arr, target)
print(result_id)











print(binary_search(arr, target))


# Search for even numbers in the range of 0, 10,000
r = range(0, 10000, 2)

if 122 in r:
    print("Found")
else:
    print("Not Found")




