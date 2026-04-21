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
        if not nums:
            return [[]] # Ask the interviewer what he wants returned here...
        
        nums.sort()
        result = []
        n = len(nums)

        def dfs(index): # Note that I DONT need to pass nums here
            if index >= n:
                result.append(nums.copy())
                return
            
            visited = set()
            
            for i in range(index, n):
                if nums[i] in visited:
                    continue
                
                visited.add(nums[i])

                nums[index], nums[i] = nums[i], nums[index]
                dfs(index + 1)
                nums[index], nums[i] = nums[i], nums[index]

        dfs(0) 

        return result

nums = [1,2,3]
print(Solution().perm(nums))
