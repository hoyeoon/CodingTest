from itertools import combinations
from collections import deque
import copy

moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + moves[i][0]
            ny = y + moves[i][1]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 1:
                continue
            if graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
                # print(nx, ny)
    return graph[n - 1][m - 1]


n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

space = []
virus = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus.append((i, j))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            space.append((i, j))

# print(graph)
# print(space)
# print(virus)
# print(list(combinations(space, 3)))
origin_graph = copy.deepcopy(graph)

max_count = 0
num = 0
for space in list(combinations(space, 3)):
    for i in range(3):
        graph[space[i][0]][space[i][1]] = 1
    # print(graph)

    for v in virus:
        bfs(v[0], v[1])

    # print(graph)

    count = 0
    for i in range(n):
        count += graph[i].count(0)

    if count > max_count:
        max_count = count

    graph = copy.deepcopy(origin_graph)

    num += 1
print(max_count)
