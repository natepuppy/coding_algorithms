# Longest Common Subsequence

# Time: O(2^(n + m)), Space: O(n + m)
def dfs(s1, s2):
    # Code will be implemented here
    pass

def dfsHelper(s1, s2, i1, i2):
    # Code will be implemented here
    pass


# Time: O(n * m), Space: O(n + m)
def memoization(s1, s2):
    # Code will be implemented here
    pass

def memoHelper(s1, s2, i1, i2, cache):
    # Code will be implemented here
    pass


# Time: O(n * m), Space: O(n + m)
def dp(s1, s2):
    # Code will be implemented here
    pass


# Time: O(n * m), Space: O(m)
def optimizedDp(s1, s2):
    # Code will be implemented here
    pass


s1 = "abcde"
s2 = "ace"
print(dfs(s1, s2))
print(memoization(s1, s2))
print(dp(s1, s2))
print(optimizedDp(s1, s2))
