nums = [1, 3, 5, 7, 7, 7, 9, 11]
target = 3

# Given a sorted array of integers. Find the leftmost occurence 
# of target, if target does not exist, return the index where it 
# would be inserted

class Solution:
    def binary_search(self, nums, target):
        L, R = 0, len(nums) # Start here in case you insert at the end.

        while L < R:
            M = (L + R) // 2

            if nums[M] >= target: # This equality is the hardest...
                R = M
            else:
                L = M + 1 # Make sure to do M here......

        return L # Dont forget return

print(Solution().binary_search(nums, target))


import bisect
# Note: nums, target - NOT (target, nums)
print(bisect.bisect_left(nums, target))  # Result: 1
print(bisect.bisect_right(nums, target)) # Result: 2 -- Which is the first index that this element could be inserted at


# Find element in rotated sorted array of integers. This array can have duplicates...

nums = [7, 9, 11, -1, 0, 0, 1, 3, 5, 7, 7]
target = 3

class Solution:
    def binary_search(self, nums, target):
        L, R = 0, len(nums) - 1

        while L <= R: # Must do <= here because I am returning -1, not L at the bottom
            M = (L + R) // 2

            if nums[M] == target:
                return M
            
            # Handle duplicate ambiguity!!!!!!!!!!!! For example:
            # [7,7,7,7,7,1,2,3,7]
            #  L       M       R
            if nums[L] == nums[M] == nums[R]:
                L += 1
                R -= 1
                continue
            # Right is sorted
            elif nums[M] <= nums[R]:  # <= here because what if nums[M] == nums[R]???
                if nums[M] < target <= nums[R]:
                    L = M + 1
                else:
                    R = M - 1
            else:  # left is sorted
                if nums[L] <= target < nums[M]:
                    R = M - 1
                else:
                    L = M + 1

        return -1

print(Solution().binary_search(nums, target))



# Search for even numbers in the range of 0, 10,000
# This is O(1) for both time and space

r = range(0, 10000, 2)

if 122 in r:
    print("Found")
else:
    print("Not Found")


