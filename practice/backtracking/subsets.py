# The Problem: Subsets (Power Set)
# Given an integer array nums of elements, 
# return all possible unique subsets (the power set).

# The solution set must not contain duplicate subsets.

# You can return the solution in any order.

# Example 1:
# Input: nums = [1, 2, 3]

# Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

# O(2^n)

class Solution:
    def sub(self, nums):
        result = []
        nums.sort()

        def dfs(arr, index):
            result.append(arr.copy())

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                
                arr.append(nums[i])
                dfs(arr, i + 1)
                arr.pop()

        dfs([], 0)

        return result


nums = [1, 1, 2, 3]
print(Solution().sub(nums))
