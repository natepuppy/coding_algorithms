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


# OR the custom way:
def binary_search(arr, target):
    L, R = 0, len(arr) - 1 # Dont forget the minus one here

    while L <= R:
        m = (L + R) // 2

        if target == arr[m]:
            return m

            # If I want to get the first occurence of 7. I need to add result = -1 above
            # Then do this here instead of returning
            # result = m      # Record the match...
            # R = m - 1       # ...but keep looking to the LEFT!

        if target < arr[m]: # Compare to arr[m], NOT m
            R = m - 1

        if target > arr[m]:
            L = m + 1
    
    return -1 # Dont forget to return -1 here

print(binary_search(arr, target))


# Search for even numbers in the range of 0, 10,000
r = range(0, 10000, 2)

if 122 in r:
    print("Found")
else:
    print("Not Found")




