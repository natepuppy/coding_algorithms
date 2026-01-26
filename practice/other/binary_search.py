import bisect

arr = [1, 3, 5, 7, 9, 11]
target = 7

# Built in way:

idx = bisect.bisect_left(arr, target)

if idx < len(arr) and arr[idx] == target:
    print(f"Found {target} at index {idx}")
else:
    print("Not found")


# OR custom way:

def binary_search(arr, target):
    # Code will be implemented here
    pass


# OR for a range of numbers:

r = range(0, 1000000, 2)

# This is instant, regardless of how large the range is
if 500250 in r:
    print("Found!")

print(binary_search(arr, target))
