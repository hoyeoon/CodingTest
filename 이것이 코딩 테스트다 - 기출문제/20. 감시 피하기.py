from itertools import combinations
from collections import deque
import copy

n = int(input())

graph, space, student = [], [], []

for i in range(n):
    graph.append(list(input().split()))
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'X':
            space.append((i, j))
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'S':
            student.append((i, j))

student_num = len(student)

moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
def bfs(x, y, i, queue):
    while queue:
        x, y = queue.popleft()
        nx = x + moves[i][0]
        ny = y + moves[i][1]

        if nx >= 0 and ny >= 0 and nx < n and ny < n:
            if graph[nx][ny] == 'T':
                return True
            elif graph[nx][ny] == 'O':
                break
            queue.append((nx, ny))
    return False

flag = 0
origin_graph = copy.deepcopy(graph)
for space in list(combinations(space, 3)):
    count = 0

    for i in range(3):
        graph[space[i][0]][space[i][1]] = 'O'

    for s in student:
        a, b = s
        r1 = bfs(a, b, 0, deque([(a, b)]))
        r2 = bfs(a, b, 1, deque([(a, b)]))
        r3 = bfs(a, b, 2, deque([(a, b)]))
        r4 = bfs(a, b, 3, deque([(a, b)]))
        if r1 == False and r2 == False and r3 == False and r4 == False:
            count += 1
    if count == student_num:
        flag = 1
        break
    graph = copy.deepcopy(origin_graph)

if flag == 1:
    print("YES")
else:
    print("NO")

# print(bfs(0, 1, 0, deque([(0, 1)])))
# print(bfs(0, 1, 1, deque([(0, 1)])))
# print(bfs(0, 1, 2, deque([(0, 1)])))
# print(bfs(0, 1, 3, deque([(0, 1)])))
