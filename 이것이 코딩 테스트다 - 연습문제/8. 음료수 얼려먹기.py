from collections import deque

answer = 0
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

print(graph)
# def dfs(x, y):
#     if x < 0 or y < 0 or x > n - 1 or y > m - 1:
#         return False
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         dfs(x-1, y)
#         dfs(x, y-1)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         return True
#     return False
#
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j) is True:
#             answer += 1
# print(answer)

# 입력 예시
# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111

d = [(-1, 0), (0, -1), (1, 0), (0, 1)] # 북 서 남 동
count = 0

for r in range(n):
    for c in range(m):
        if graph[r][c] == 0:
            count += 1
            print("r, c =", r, " ", c)
            queue = deque()
            queue.append((r, c))
            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    nx = x + d[i][0]
                    ny = y + d[i][1]

                    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 1 and graph[nx][ny] == 0:
                        queue.append((nx, ny))
                        graph[nx][ny] = 2


print(graph)
print(count)