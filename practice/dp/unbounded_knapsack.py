# Given a list of N items, and a backpack with a
# limited capacity, return the maximum total profit that 
# can be contained in the backpack. The i-th item's profit
# is profit[i] and it's weight is weight[i]. Assume you can
# have an unlimited number of each item available. 

from functools import cache

class Solution:
    def top_down(self, profits, weights, capacity):
        
        @cache
        def dfs(i, rem_capacity):
            if i >= len(profits):
                return 0
            
            # Without i
            profit_without = dfs(i + 1, rem_capacity)

            # With i
            profit_with = 0
            if rem_capacity - weights[i] >= 0: # Use >= NOT > !!!!!
                profit_with = profits[i] + dfs(i, rem_capacity - weights[i])

            return max(profit_without, profit_with)

        
        return dfs(0, capacity)



    def bottom_up(self, profits, weights, capacity):
        dp = [0] * (capacity + 1)

        for i in range(len(profits)):
            profit = profits[i]
            weight = weights[i]

            for j in range(weight, capacity + 1):
                dp[j] = max(dp[j], dp[j - weight] + profit)
        
        return dp[capacity]
        


profits = [15, 50, 60, 90]
weights = [1, 3, 4, 5]
capacity = 8

print(Solution().top_down(profits, weights, capacity))
print(Solution().bottom_up(profits, weights, capacity))
















'''

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
                profit_2 = dfs(index, cap - weights[index]) + profits[index]

            max_profit = max(profit_1, profit_2)
            cache[(index, cap)] = max_profit # DONT FORGET to update cache!!!!!
            
            return max_profit

        return dfs(0, capacity)

    def bottom_up(self, profits, weights, capacity):
        dp = [0] * (capacity + 1)

        for i in range(capacity + 1):
            for j in range(len(profits)):
                weight = weights[j]
                profit = profits[j]

                if weight > i:
                    continue
                
                new_profit = profit + dp[i - weight]

                dp[i] = max(dp[i], new_profit)
        
        return dp[capacity]

'''