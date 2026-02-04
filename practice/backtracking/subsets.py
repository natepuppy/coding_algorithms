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
    result = []

    def dfs(index, subset):
        if index == len(nums):
            result.append(subset.copy())
            return

        subset.append(nums[index])
        dfs(index + 1, subset)
        subset.pop()

        dfs(index + 1, subset)

    dfs(0, [])
    return result

# multi-branch recursion
# With duplicate skipping
def subsets2(nums):
    result = []

    def dfs(index, subset):
        result.append(subset.copy())

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()

    dfs(0, [])
    return result

nums = [1, 1, 2, 3]
print(subsets1(nums))
print(subsets2(nums))
