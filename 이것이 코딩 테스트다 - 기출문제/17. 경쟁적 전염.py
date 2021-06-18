from collections import deque

n, k = map(int, input().split())
graph =[]
for i in range(n):
    graph.append(list(map(int, input().split())))
target_s, target_x, target_y = map(int, input().split())

moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]

virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 x, 위치 y)
            virus.append((graph[i][j], 0, i, j))
virus.sort() # 오름차순
print(virus)

queue = deque(virus)

# queue가 빌 때까지 반복
while queue:
    print(queue)
    virus, s, x, y = queue.popleft()

    # s초가 지나면 반복문 탈출
    if s == target_s:
        break
    for i in range(4):
        nx = x + moves[i][0]
        ny = y + moves[i][1]

        if nx >= 0 and ny >= 0 and nx < n and ny < n:
            if graph[nx][ny] == 0:
                queue.append((virus, s + 1, nx, ny))
                graph[nx][ny] = graph[x][y] # graph[nx][ny] = virus

print(graph[target_x - 1][target_y - 1])
