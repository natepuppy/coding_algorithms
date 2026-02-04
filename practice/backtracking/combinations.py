# Given an array nums, return all distinct combinations whose elements sum to k.
# Each element may be used at most once.
# The result must not contain duplicate combinations.

def combinationSum2(nums, k):
    nums.sort()
    result = []

    def dfs(index, curr_nums, curr_sum):
        if curr_sum > k:
            return

        if curr_sum == k:
            result.append(curr_nums.copy())
            return

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue

            curr_nums.append(nums[i])
            curr_sum += nums[i]

            dfs(i + 1, curr_nums, curr_sum)

            curr_sum -= nums[i]
            curr_nums.pop()

    dfs(0, [], 0)
    return result

nums = [1, 2, 3, 1, 6, 4]
# nums = [1,1,2,3,4]
k = 7

print(combinationSum2(nums, k))
