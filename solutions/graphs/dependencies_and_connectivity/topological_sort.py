from collections import defaultdict

# Use when you have a strict set of prerequisites and need
# to find a valid chronological order to complete them.
def topologicalSort(num_courses, prereqs):
    graph = defaultdict(lambda: [])
    for course, prereq in prereqs:
        graph[course].append(prereq)

    result = []
    visited = set()
    acyclic = True

    def dfs(i, current_visited):
        nonlocal acyclic
        if i in current_visited or not acyclic:
            acyclic = False
            return
        if i in visited:
            return

        current_visited.add(i)
        
        for prereq in graph[i]:
            dfs(prereq, current_visited)
        
        current_visited.remove(i)
        
        visited.add(i)
        result.append(i)
    
    for i in range(num_courses):
        if i not in visited:
            dfs(i, set())
            if not acyclic:
                return []

    return result




from collections import deque

# To increase performace, replace the dictionaries with lists.
def kahns(num_courses, prereqs):
    pass
    # adj: maps a prerequisite to the courses that depend on it
    # in_degree: tracks how many prerequisites each course has left
    graph = {}
    degree = {}
    for i in range(num_courses):
        graph[i] = []
        degree[i] = 0

    # Note: I am building this in the direction of Prereq: [child courses]
    for course, prereq in prereqs:
        graph[prereq].append(course)
        degree[course] += 1
    
    # Add all course with no prereqs into the queue
    queue = deque([])
    for key, value in degree.items():
        if value == 0:
            queue.append(key)
    
    result = []

    while queue:
        curr_course = queue.popleft()
        result.append(curr_course)

        for neighbor in graph[curr_course]:
            degree[neighbor] -= 1

            if degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(result) < num_courses:
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
print(kahns(num_courses, prereqs))
# Output: [1, 3, 2, 4]
