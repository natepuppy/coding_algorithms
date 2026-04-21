from collections import defaultdict

# Use when you have a strict set of prerequisites and need
# to find a valid chronological order to complete them.
def topologicalSort(num_courses, prereqs):
    graph = defaultdict(list)
    for course, pre in prereqs:
        graph[course].append(pre)
    
    result = []
    visited = set()
    visiting = set()

    def dfs(node):
        if node in visiting:
            return False
        if node in visited:
            return True
        
        visiting.add(node)

        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False # Dont forget this return!!!!!

        result.append(node)
        visiting.remove(node)
        visited.add(node) # This goes after...

        return True

    for i in range(num_courses):
        if i not in visited: # Small optimization
            if not dfs(i):
                return []

    return result


# Return a valid ordering of courses you can take to finish all courses.
# [0, 1], indicates that to take course 0 you have to first take course 1.
# Courses are labeled 0 to num_courses - 1
# Input: num_courses = 3, prereqs = [[0,1],[1,2],[2,0]]
# Output: [0,1,2]

num_courses = 4
prereqs = [[0, 1], [2, 1], [3, 0], [3, 2]]

print(topologicalSort(num_courses, prereqs))
# print(kahns(num_courses, prereqs))
# Output: [1, 3, 2, 4]

