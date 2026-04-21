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



import heapq
result = heapq.nlargest(k, nums)[-1]


# bisect.bisect_left(nums, target)


# how to loop through a dict with .items()


nlargest



# Remember, there are no max heaps...
