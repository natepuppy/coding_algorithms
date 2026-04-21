from collections import defaultdict


num_courses = 3
prereqs = [[0, 1], [1, 2]]

# Use when you have a strict set of prerequisites and need
# to find a valid chronological order to complete them.
def topologicalSort(num_courses, prereqs):
    graph = defaultdict(list)
    for course, prereq in prereqs:
        graph[course].append(prereq) # Double check

    visited = set()
    visiting = set()
    result = []

    def dfs(node):
        if node in visiting:
            return False
        if node in visited:
            return True
        
        visiting.add(node)

        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False
        
        visiting.remove(node)
        visited.add(node)
        result.append(node)

        return True

    for i in range(num_courses):
        if i not in visited:
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












# from collections import deque

# # To increase performace, replace the dictionaries with lists.
# def kahns(num_courses, prereqs):
#     pass
#     # adj: maps a prerequisite to the courses that depend on it
#     # in_degree: tracks how many prerequisites each course has left
#     graph = {}
#     degree = {}
#     for i in range(num_courses):
#         graph[i] = []
#         degree[i] = 0

#     # Note: I am building this in the direction of Prereq: [child courses]
#     for course, prereq in prereqs:
#         graph[prereq].append(course)
#         degree[course] += 1
    
#     # Add all course with no prereqs into the queue
#     queue = deque([])
#     for key, value in degree.items():
#         if value == 0:
#             queue.append(key)
    
#     result = []

#     while queue:
#         curr_course = queue.popleft()
#         result.append(curr_course)

#         for neighbor in graph[curr_course]:
#             degree[neighbor] -= 1

#             if degree[neighbor] == 0:
#                 queue.append(neighbor)
    
#     if len(result) < num_courses:
#         return []
    
#     return result



