# n x m 2차행렬
# x = x + 1, y = y + 1 방향으로 이동
# 만약 x, y 가 행렬 범위 벗어나면 x = (x + 1) % n, y = (y + 1) % m
# 전체 돌았는데 만약 방문하지 않은 곳이 있으면 return false
# 전체 방문했으면 return true
# ex. [[0, 0], [0, 0]]의 경우 false(계속 돌아도 [[1, 0], [0, 1]] 이므로)
# 시간초과로 38/100 (효율성을 더 생각해봐야할 것 같음)
# x, y 개수가 31 제곱수였음.

from collections import deque

def solution(x, y):
    direction = (1, 1)
    city = []
    visited = [0] * (x * y)
    for i in range(x):
        city.append(y * [0])

    queue = deque()
    queue.append((0, 0))
    count = 0

    while queue:
        r, c = queue.popleft()
        nr = r + direction[0]
        nc = c + direction[1]

        if nr >= x or nc >= y or nr < 0 or nc < 0:
            nr = nr % x
            nc = nc % y

        if city[nr][nc] == 0 and city[nr][nc] != 1:
            city[nr][nc] = 1
            queue.append((nr, nc))
            visited[count] = 1
            count += 1

    if 0 in visited :
        return False
    return True