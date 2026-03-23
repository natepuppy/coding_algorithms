# The Problem: Subsets (Power Set)
# Given an integer array nums of elements, 
# return all possible unique subsets (the power set).

# The solution set must not contain duplicate subsets.

# You can return the solution in any order.

# Example 1:
# Input: nums = [1, 2, 3]

# Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

# Two branch recursion
def subsets1(nums):
    

# multi-branch recursion
# With duplicate skipping
def subsets2(nums):
    

nums = [1, 1, 2, 3]
print(subsets1(nums))
print(subsets2(nums))
