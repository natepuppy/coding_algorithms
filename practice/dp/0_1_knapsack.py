# Given a list of N items, and a backpack with a
# limited capacity, return the maximum total profit that 
# can be contained in the backpack. The i-th item's profit
# is profit[i] and it's weight is weight[i]. Assume you can
# only add each item to the bag at most one time.

class Solution:
    def top_down(self, profits, weights, capacity):
        cache = {}
        n = len(profits)

        def dfs(index, cap):
            if index == n or cap == 0:
                return 0
            
            if (index, cap) in cache:
                return cache[(index, cap)]

            profit_1 = dfs(index + 1, cap)

            profit_2 = 0
            if cap - weights[index] >= 0:
                profit_2 = dfs(index + 1, cap - weights[index]) + profits[index]

            max_profit = max(profit_1, profit_2)
            cache[(index, cap)] = max_profit
            
            return max_profit

        return dfs(0, capacity)
    
    def bottom_up(self, profits, weights, capacity):
        dp = [0] * (capacity + 1)

        for i in range(len(profits)):
            profit = profits[i]
            weight = weights[i]

            for j in reversed(range(weight, capacity + 1)):
                new_profit = profit + dp[j - weight]
                dp[j] = max(dp[j], new_profit)
        
        return dp[capacity]


profits = [4, 4, 7, 1]
weights = [5, 2, 3, 1]
capacity = 8

print(Solution().top_down(profits, weights, capacity))
print(Solution().bottom_up(profits, weights, capacity))
