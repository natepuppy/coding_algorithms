# Implementation of MergeSort

# Why pass these in as params?
#  - In many languages (like Python), slicing creates a copy of the data.
#  - 

# Check self...
class Solution:
    def __init__(self, nums):
        self.nums = nums

    def run(self):
        L, R = 0, len(self.nums) - 1
        return self.merge_sort(L, R)
    
    def merge(self, left, right):
        result = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result += left[i:len(left)] or right[j:len(right)]

        return result

    def merge_sort(self, L, R):
        if L == R:
            return [self.nums[L]]
        
        M = (L + R) // 2
        
        left = self.merge_sort(L, M)
        right = self.merge_sort(M + 1, R)

        return self.merge(left, right)
        

nums = [9, 20, 5, 2, 4, 6, 1, 3, 7, 8, 0, 30, -1, -20]

print(Solution(nums).run())
