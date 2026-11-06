from collections import defaultdict
from collections import deque

# A course can start only when every prerequisite is finished.
# Kahn's repeatedly takes the courses that currently have none left.
def kahns(num_courses, prereqs):
    graph = defaultdict(list)
    num_prereqs = [0] * num_courses

    for course, prereq in prereqs:
        graph[prereq].append(course) # Come back to this
        num_prereqs[course] += 1
    
    queue = deque()
    for i in range(len(num_prereqs)):
        if num_prereqs[i] == 0:
            queue.append(i)
    
    result = []
    visited = set()

    while queue:
        node = queue.popleft()

        result.append(node)

        for course in graph[node]:
            num_prereqs[course] -= 1
            if num_prereqs[course] == 0: # Prevents something from being enqueued twice
                queue.append(course)
        
    if len(result) != num_courses:
        return []
    
    return result
        
        




        
    


# Same setup as topological sort.
# [0, 1] means course 0 requires course 1.
# Courses are labeled 0 to num_courses - 1.

num_courses = 4
prereqs = [[0, 1], [2, 1], [3, 0], [3, 2]]

print(kahns(num_courses, prereqs))
# Output: [1, 0, 2, 3]

print(kahns(3, [[0, 1], [1, 2], [2, 0]]))
# Output: []  cycle, no valid order


















'''

def kahns(num_courses, prereqs):
    graph = defaultdict(list)
    indegree = [0] * num_courses

    for course, prereq in prereqs:
        graph[prereq].append(course)
        indegree[course] += 1

    queue = deque(i for i in range(num_courses) if indegree[i] == 0)
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != num_courses:
        return []

    return result

'''