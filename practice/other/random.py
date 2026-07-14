import random

x = random.randint(1, 10)  # inclusive
print(x)


from functools import cache

@cache  # Exactly identical to @lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n-1) + fibonacci(n-2)


from sortedcontainers import SortedDict
sorted_map = SortedDict(
    {
        'c': 3, 
        'a': 1, 
        'b': 2
    }
)

print(sorted_map) # Output: {'a': 1, 'b': 2, 'c': 3}


# Sort by second element in tuple:
data = [("apple", 10), ("banana", 5), ("cherry", 8)]
sorted_data = sorted(data, key=lambda x: x[1])
# ALSO...
points = [(2,3),(4,2),(5,6)]
points.sort(key=lambda x: x[0]**2 + x[1]**2)

intervals.sort(key=lambda x: (x[0], -x[1]))



char = 'c'
index = ord(char) - ord('a') # Output: 2


# One liner to create matrix
matrix = [[0] * COLS for _ in range(ROWS)]


arr = ["ab", "bc", "cd"]
result = "".join(arr)
print(result)  # Output: "abbccd"


str.isalnum()
str.isalpha()
str.isdigit()
str.isdecimal()
str.isspace()

str.lower()




# Remember, there are no max heaps...
import heapq
result = heapq.nlargest(k, nums)[-1]




# n & (n - 1) removes the lowest set bit


# how to sort a string:
s = "acb"
sorted(s) # outputs "abc"


# a list [1,2,3,4,5] is not hashable for a dict in python. Instead convert it to a tuple:
tuple(count)
tuple([1, 2, 3, 4, 5]) # Output: (1, 2, 3, 4, 5)



# Counting Bits    

n = 13

n = -1
# built in ways:
print(n.bit_count())
# OR
print(bin(n).count('1'))




# Loop through all key and values in a hash map
for key, value in counts.items():
  buckets[value].append(key)


# These are the same:
for key in my_dict.keys():
    print(key)
for key in my_dict:
    print(key)

# Loop over values:
for value in my_dict.values():
    print(value)

# Turn all the values of a hash map into a list
list(my_dict.values())


# Built IN!!!!!!!!!!!!!!!!!!!!
        

from disjoint_set import DisjointSet

ds = DisjointSet()

# It creates elements on the fly as you use them
ds.union(1, 2)
ds.union(2, 3)

# Check connectivity
print(ds.connected(1, 3)) # Output: True
print(ds.connected(1, 4)) # Output: False

# Find the root
print(ds.find(1))


import bisect
# Note: nums, target - NOT (target, nums)6
print(bisect.bisect_left(nums, target))  # Result: 1
print(bisect.bisect_right(nums, target)) # Result: 2 -- Which is the first index that this element could be inserted at
bisect.insort([1,2,4,5,6], 3) # inserts in sorted order

float("inf")
float("-inf")

# Search for even numbers in the range of 0, 10,000
# This is O(1) for both time and space

r = range(0, 10000, 7)

if 127 in r:
    print("Found")
else:
    print("Not Found")






