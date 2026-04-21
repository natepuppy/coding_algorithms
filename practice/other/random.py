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

