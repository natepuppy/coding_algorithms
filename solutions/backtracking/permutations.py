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

def permutations(nums):
    result = []

    def dfs(index):
        if index == len(nums) - 1:
            result.append(nums.copy())
            return
        
        for i in range(index, len(nums)):
            nums[index], nums[i] = nums[i], nums[index] # Swap the numbers
            dfs(index + 1)
            nums[index], nums[i] = nums[i], nums[index]

    dfs(0)
    
    return result

nums = [1,2,3]
print(permutations(nums))
