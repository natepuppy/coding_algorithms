nums = [1, 7, 7, 7, 7, 7, 7, 11]
target = 7

# Given a sorted array of integers. Find the leftmost/rightmost occurence 
# of target, if target does not exist, return the index where it 
# would be inserted

def binary_search_left(nums, target):
    if not nums:
        return 0
    
    n = len(nums)
    L, R = 0, n

    while L < R:
        M = (L + R) // 2

        if nums[M] < target: # THIS IS THE ONLY LINE THAT IS DIFFERENT
            L = M + 1
        else:
            R = M
    
    return L # Always return left
            
def binary_search_right(nums, target):
    if not nums:
        return 0
    
    n = len(nums)
    L, R = 0, n

    while L < R:
        M = (L + R) // 2

        if nums[M] <= target:
            L = M + 1
        else:
            R = M
    
    return L


print(binary_search_left(nums, target))
print(binary_search_right(nums, target))



# Find element in rotated sorted array of integers

nums = [7, 9, 11, -1, 0, 0, 1, 3, 5, 7, 7]
target = 3

class Solution:
    def binary_search(self, nums, target):
        L, R = 0, len(nums) - 1

        while L <= R:
            M = (L + R) // 2

            if nums[M] == target:
                return M
            
            # This handles duplicates:
            # EX: [1, 0, 1, 1, 1]
            if nums[L] == nums[M] == nums[R]:
                L += 1
                R -= 1
                continue

            if nums[M] < nums[R]: # right it sorted
                if nums[M] < target <= nums[R]:
                    L = M + 1
                else:
                    R = M - 1
            else: # left is sorted
                if nums[L] <= target < nums[M]:
                    R = M - 1
                else:
                    L = M + 1
        
        return -1 # 

print(Solution().binary_search(nums, target))





