# Given a list of N items, and a backpack with a
# limited capacity, return the maximum total profit that 
# can be contained in the backpack. The i-th item's profit
# is profit[i] and it's weight is weight[i]. Assume you can
# only add each item to the bag at most one time.

from functools import cache

class Solution:
    def top_down(self, profits, weights, capacity):
        @cache
        def dfs(i, rem_capacity):
            if i == len(profits):
                return 0

            # include i
            profit_with = 0
            if rem_capacity - weights[i] >= 0:
                profit_with = profits[i] + dfs(i + 1, rem_capacity - weights[i])

            # dont include i
            profit_without = dfs(i + 1, rem_capacity)

            return max(profit_with, profit_without)

        return dfs(0, capacity)

    def bottom_up(self, profits, weights, capacity):
        dp = [0] * (capacity + 1)

        for i in range(len(profits)):
            profit = profits[i]
            weight = weights[i]

            # MUST DO REVERED HERE, or else you could use the same element twice!!!
            for j in reversed(range(weight, capacity + 1)):
                dp[j] = max(dp[j], dp[j - weight] + profit)
        
        return dp[capacity]

profits = [4, 4, 7, 1]
weights = [5, 2, 3, 1]
capacity = 8

print(Solution().top_down(profits, weights, capacity))
print(Solution().bottom_up(profits, weights, capacity))


















'''


    
    def bottom_up(self, profits, weights, capacity):
        dp = [0] * (capacity + 1)

        for i in range(len(profits)):
            profit = profits[i]
            weight = weights[i]

            for j in reversed(range(weight, capacity + 1)):
                new_profit = profit + dp[j - weight]
                dp[j] = max(dp[j], new_profit)
        
        return dp[capacity]


'''

