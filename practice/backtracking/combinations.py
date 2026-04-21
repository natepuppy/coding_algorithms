# Given an array nums, return all distinct combinations whose elements sum to k.
# Each element may be used at most once.
# The result must not contain duplicate combinations.

# Can input have negatives? Yes

# O(n choose k) or 2^n

class Solution:
    def comb(self, nums, k):
        if not nums:
            return []

        n = len(nums)
        nums.sort()
        result = []

        def dfs(index, curr_sum, curr_arr): # Three params
            if curr_sum == k:
                result.append(curr_arr.copy())
                return # Remove for negatives...
            
            if curr_sum > k: # Remove for negatives...
                return
            
            for i in range(index, n):
                num = nums[i]
                if i > index and num == nums[i - 1]:
                    continue
                
                curr_arr.append(num)
                dfs(i + 1, curr_sum + num, curr_arr)
                curr_arr.pop()

        dfs(0, 0, [])
        
        return result





nums = [1, 2, 3, 1, 6, 4]
k = 7

print(Solution().comb(nums, k))




















        # result = []
        # nums.sort()

        # # Note: pass curr_sum -- sum(arr) is a O(n) operation
        # def dfs(index, curr_sum, arr):
        #     if curr_sum == k:
        #         result.append(arr.copy())
        #         # return # Removing this allows it to work for negatives

        #     for i in range(index, len(nums)):
        #         if i > index and nums[i] == nums[i - 1]:
        #             continue

        #         new_sum = curr_sum + nums[i]

        #         # Filter out here for better efficiency
        #         # if new_sum > k: # Removing this allows it to work for negatives
        #         #     break

        #         arr.append(nums[i])
        #         dfs(i + 1, new_sum, arr)
        #         arr.pop()

        # dfs(0, 0, [])

        # return result


