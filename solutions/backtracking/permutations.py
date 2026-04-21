# Given a collection of numbers, nums, that might contain 
# duplicates, return all possible unique permutations in any order.
# EX:
# Input: nums = [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

# O(n!)

class Solution:
    def perm(self, nums):
        result = []
        n = len(nums)

        # Only one Param!!!
        def dfs(index):
            if index == n:
                result.append(nums.copy())
                return

            visited = set()
            
            for i in range(index, n):
                if nums[i] in visited:
                    continue

                visited.add(nums[i]) # Make sure to do this first before you switch everything
                    
                nums[i], nums[index] = nums[index], nums[i]
                dfs(index + 1)
                nums[i], nums[index] = nums[index], nums[i]
                

        dfs(0)

        return result

        

nums = [1,2,3]
print(Solution().perm(nums))
