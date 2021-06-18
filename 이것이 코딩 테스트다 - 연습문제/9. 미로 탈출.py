# from collections import deque
#
# n, m = map(int, input().split())
#
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
#
# print(graph)
# moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
#
# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y))
#
#     while queue:
#         x, y = queue.popleft()
#
#         for i in range(4):
#             nx = x + moves[i][0]
#             ny = y + moves[i][1]
#
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 continue
#             if graph[nx][ny] == 0:
#                 continue
#             if graph[nx][ny] == 1:
#                 queue.append((nx, ny))
#                 graph[nx][ny] = graph[x][y] + 1
#                 print(nx, ny)
#     # print(graph)
#     return graph[n - 1][m - 1]

# 입력
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

from collections import deque
n, m = map(int, input().split())
miro = []
for i in range(n):
    miro.append(list(map(int, input())))
print(miro)

d = [(-1, 0), (0, -1), (1, 0), (0, 1)] # 북 서 남 동

queue = deque()
queue.append((0, 0))
while queue:
    x, y = queue.popleft()
    print(x, y)

    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if 0 <= nx < n and 0 <= ny < m and miro[nx][ny] != 0 and miro[nx][ny] == 1:
            queue.append((nx, ny))
            miro[nx][ny] = miro[x][y] + 1

print(miro)

# bfs(0, 0)
# print(graph)