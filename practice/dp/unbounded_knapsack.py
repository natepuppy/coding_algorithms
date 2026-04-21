# Given a list of N items, and a backpack with a
# limited capacity, return the maximum total profit that 
# can be contained in the backpack. The i-th item's profit
# is profit[i] and it's weight is weight[i]. Assume you can
# have an unlimited number of each item available. 



profits = [15, 50, 60, 90]
weights = [1, 3, 4, 5]
capacity = 8

print(top_down(profits, weights, capacity))
print(bottom_up(profits, weights, capacity))
