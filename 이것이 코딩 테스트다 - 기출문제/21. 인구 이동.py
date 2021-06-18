from collections import deque
n, l, r = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# print(graph)

moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
def bfs(x, y, index):
    # (x, y)의 위치와 연결된 나라(연합)정보를 담는 리스트
    united = []
    united.append((x, y))

    queue = deque()
    queue.append((x, y))

    union[x][y] = index # 현재 연합의 번호 할당
    pnum = graph[x][y] # 현재 연합의 전체 인구 수
    inum = 1 # 현재 연합의 국가 수

    # 큐가 빌 때까지 반복(BFS)
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + moves[i][0]
            ny = y + moves[i][1]

            # 바로 옆에 있는 나라를 확인
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    queue.append((nx, ny))

                    # 연합에 추가
                    union[nx][ny] = index
                    pnum += graph[nx][ny]
                    inum += 1
                    united.append((nx, ny))

    # 연합 국가끼리 인구 분배
    for i, j in united:
        graph[i][j] = pnum // inum
    return inum

move_count = 0

while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                bfs(i, j, index)
                index += 1
               # print(union)
    # 모든 인구 이동이 끝난 경우
    if index == n * n:
        break
    move_count += 1
    #print(move_count)
#print(union)
print(move_count)
# union = [[-1] * n for _ in range(n)]
# print(bfs(1, 2, 0))
# print(union)