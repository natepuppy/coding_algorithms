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
        n = len(nums)
        result = []
        nums.sort() # Dont forget sort

        def dfs(index, arr):
            # no base case needed
            result.append(arr.copy()) # Dont forget copy

            for i in range(index, n):
                if i > index and nums[i] == nums[i - 1]: # If not while
                    continue

                arr.append(nums[i])
                dfs(i + 1, arr)
                arr.pop()

        dfs(0, [])

        return result

        

nums = [1, 2, 3]
print(Solution().sub(nums))
