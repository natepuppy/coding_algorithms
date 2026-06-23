import random

x = random.randint(1, 10)  # inclusive
print(x)



# Sort by second element in tuple:
data = [("apple", 10), ("banana", 5), ("cherry", 8)]
sorted_data = sorted(data, key=lambda x: x[1])
# ALSO...
points = [(2,3),(4,2),(5,6)]
points.sort(key=lambda x: x[0]**2 + x[1]**2)



c = 'A'
value = ord(c)
print(value)  # Output: 65


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


edges.sort(key=lambda x: x[2])


# Remember, there are no max heaps...
import heapq
result = heapq.nlargest(k, nums)[-1]


# bisect.bisect_left(nums, target)


# how to loop through a dict with .items()


nlargest


intervals.sort(key=lambda x: x[0])



# n & (n - 1) removes the lowest set bit


index = ord(char) - ord('a')


# Return all the groups as a list of lists
list(dict.values())




# how to sort a string:
s = "acb"
sorted(s) # outputs "abc"


# a list [1,2,3,4,5] is not hashable for a dict in python. Instead convert it to a tuple:
tuple(count)




# get int representation of a char:
ord(char) - ord('a')



# Counting Bits    

n = 13

print(countBits(n))

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
list(mp.values())


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
# Note: nums, target - NOT (target, nums)
print(bisect.bisect_left(nums, target))  # Result: 1
print(bisect.bisect_right(nums, target)) # Result: 2 -- Which is the first index that this element could be inserted at



# Search for even numbers in the range of 0, 10,000
# This is O(1) for both time and space

r = range(0, 10000, 2)

if 122 in r:
    print("Found")
else:
    print("Not Found")



envelopes.sort(key=lambda x: (x[0], -x[1]))




