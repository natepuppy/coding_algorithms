# Given a list of N items, and a backpack with a
# limited capacity, return the maximum total profit that 
# can be contained in the backpack. The i-th item's profit
# is profit[i] and it's weight is weight[i]. Assume you can
# only add each item to the bag at most one time.

# def top_down(profits, weights, cap):
#     def dfs(index, curr_profit, rem_cap):
#         if rem_cap == 0:
#             return curr_profit
#         if rem_cap < 0:
#             return 0
#         if index >= len(weights):
#             return curr_profit

#         without_el = dfs(index + 1, curr_profit, rem_cap)

#         rem_cap -= weights[index]
#         curr_profit += profits[index]
#         with_el = dfs(index + 1, curr_profit, rem_cap)

#         return max(without_el, with_el)

#     return dfs(0, 0, cap)

def top_down(profits, weights, cap):
    memo = {}

    def dfs(index, rem_cap):
        if index == len(weights):
            return 0

        if (index, rem_cap) in memo:
            return memo[(index, rem_cap)]
        
        # Dont add
        result = dfs(index + 1, rem_cap)

        # Add it
        if weights[index] <= rem_cap:
            result_with = profits[index] + dfs(index + 1, rem_cap - weights[index])
            result = max(result, result_with)
        
        memo[(index, rem_cap)] = result

        return result

    return dfs(0, cap)
    

def bottom_up(profits, weights, cap):
    

profits = [4, 4, 7, 1]
weights = [5, 2, 3, 1]
capacity = 8

print(top_down(profits, weights, capacity))
print(bottom_up(profits, weights, capacity))


























# profits = [4, 4, 7, 1]
# weights = [5, 2, 3, 1]
# capacity = 8

# [0,0,0,0,0,0,0,0,0]
# [0,0,0,0,0,0,0,0,0]


















