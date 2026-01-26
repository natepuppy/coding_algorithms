# Given a list of N items, and a backpack with a
# limited capacity, return the maximum total profit that 
# can be contained in the backpack. The i-th item's profit
# is profit[i] and it's weight is weight[i]. Assume you can
# only add each item to the bag at most one time. 

# Brute force Solution
# Time: O(2^n), Space: O(n)
# Where n is the number of items.
def dfs(profit, weight, capacity):
    # Code will be implemented here
    pass

def dfsHelper(i, profit, weight, capacity):
    # Code will be implemented here
    pass


# Memoization Solution
# Time: O(n * m), Space: O(n * m)
# Where n is the number of items & m is the capacity.
def memoization(profit, weight, capacity):
    # Code will be implemented here
    pass

def memoHelper(i, profit, weight, capacity, cache):
    # Code will be implemented here
    pass


# Dynamic Programming Solution
# Time: O(n * m), Space: O(n * m)
# Where n is the number of items & m is the capacity.
def dp(profit, weight, capacity):
    # Code will be implemented here
    pass


# Memory optimized Dynamic Programming Solution
# Time: O(n * m), Space: O(m)
def optimizedDp(profit, weight, capacity):
    # Code will be implemented here
    pass


profits = [1, 6, 10, 16]
weights = [1, 2, 3, 5]
capacity = 7

print(dfs(profits, weights, capacity))
print(memoization(profits, weights, capacity))
print(dp(profits, weights, capacity))
print(optimizedDp(profits, weights, capacity))
