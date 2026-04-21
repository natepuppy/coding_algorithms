def quick_sort(nums):
    if not nums:
        return nums
    
    def sort(L, R):
        if L >= R:
            return
        
        pivot_val = nums[R]
        pivot = L

        for i in range(L, R):
            if nums[i] <= pivot_val:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                pivot += 1

        # place pivot in final correct position!!!!!!!!!!!!!!!!
        nums[pivot], nums[R] = nums[R], nums[pivot]
        
        sort(L, pivot - 1)
        sort(pivot + 1, R)
    
    L, R = 0, len(nums) - 1
    sort(L, R)

    return nums
    
nums = [1, 1, 4, 6, 1, 3]
print(quick_sort(nums))
