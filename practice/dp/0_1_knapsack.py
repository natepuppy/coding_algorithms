# Given a list of N items, and a backpack with a
# limited capacity, return the maximum total profit that 
# can be contained in the backpack. The i-th item's profit
# is profit[i] and it's weight is weight[i]. Assume you can
# only add each item to the bag at most one time. 

def top_down(profits, weights, cap):
    dp = {}

    def dfs(index, remaining_cap):
        if index == len(profits) or remaining_cap <= 0:
            return 0
        
        if (index, remaining_cap) in dp:
            return dp[(index, remaining_cap)]
        
        # Dont add it
        profit = dfs(index + 1, remaining_cap)

        # If it can fit, add it
        if weights[index] <= remaining_cap:
            res = profits[index] + dfs(index + 1, remaining_cap - weights[index])
            profit = max(profit, res)

        dp[(index, remaining_cap)] = profit

        return profit

    return dfs(0, capacity)

# BASE CASE ILLUSTRATION
# The first row and first column stay 0 to represent "No Items" or "No Capacity".
#
# [
#  Col: 0  1  2  3  4  5  6  7  8   (Capacity)
#     [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ], # Row 0: Dummy/Base Case
#     [ 0, ., ., ., ., ., ., ., . ], # Row 1: Item 1
#     [ 0, ., ., ., ., ., ., ., . ], # Row 2: Item 2
#     [ 0, ., ., ., ., ., ., ., . ], # Row 3: Item 3
#     [ 0, ., ., ., ., ., ., ., . ]  # Row 4: Item 4
# ]
# 
# [
#     [0, 0, 0, 0, 0,  0,  0,  0,  0], 
#     [0, 0, 0, 0, 0,  4,  4,  4,  4], 
#     [0, 0, 4, 4, 4,  4,  4,  8,  8], 
#     [0, 0, 4, 7, 7, 11, 11, 11, 11], 
#     [0, 1, 4, 7, 8, 11, 12, 12, 12]
# ]
# 
# [
#     [0, 0, 0, 0, 0,  0,  0,  0,  0], 
#     [0, 0, 0, 0, 0,  4,  4,  4,  4], 
#     [0, 0, 4, 4, 4,  4,  4,  8,  8], 
#     [0, 0, 4, 7, 7, 11, 11, 11, 11], 
#     [0, 1, 4, 7, 8, 11, 12, 12, 12]
# ]
def bottom_up(profits, weights, cap):
    ROWS, COLS = len(weights) + 1, cap + 1
    dp = [[0] * COLS for _ in range(ROWS)]

    for r in range(1, ROWS):
        current_weight = weights[r - 1]
        current_profit = profits[r - 1]

        for c in range(1, COLS):
            skip = dp[r - 1][c]

            include = 0
            if c - current_weight >= 0:
                # LOOK UP ONE ROW!!
                # Look left the distance of current_weight
                include = current_profit + dp[r - 1][c - current_weight]
            
            dp[r][c] = max(skip, include)

    return dp[ROWS - 1][COLS - 1]

profits = [4, 4, 7, 1]
weights = [5, 2, 3, 1]
capacity = 8

print(top_down(profits, weights, capacity))
print(bottom_up(profits, weights, capacity))
