# 입력 예시1
# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D

# 입력 예시2
# 10
# 4
# 1 2
# 1 3
# 1 4
# 1 5
# 4
# 8 D
# 10 D
# 11 D
# 13 L

# 입력 예시3
# 10
# 5
# 1 5
# 1 3
# 1 2
# 1 6
# 1 7
# 4
# 8 D
# 10 D
# 11 D
# 13 L

n = int(input())
k = int(input())
# 뱀 시작 위치 자체가 1, 1이니깐 인덱스랑 맞추는 게 좋을 것 같다.
board = [[0] * (n + 1) for _ in range(n + 1)]
info = [] # 방향 회전 정보

for i in range(k):
    x, y = map(int, input().split())
    board[x][y] = 2 # 사과를 2로 표시

# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 방향(동, 남, 서, 북)
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def simulate():
    row, col = 1, 1 # 뱀의 머리 위치
    board[row][col] = 1 # 뱀이 존재하는 위치를 1로 표시
    direction = 0 # 초기 방향(처음에는 동쪽을 보고 있음)
    time = 0
    index = 0 # 다음에 회전할 정보
    q = [(row, col)]  # 뱀이 차지하는 위치 정보(0번 인덱스는 꼬리)

    while True:
        nrow = row + d[direction][0]
        ncol = col + d[direction][1]

        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nrow <= n and 1 <= ncol <= n and board[nrow][ncol] != 1:
            # 사과가 없다면 이동 후에 꼬리 제거
            if board[nrow][ncol] == 0:
                board[nrow][ncol] = 1
                q.append((nrow, ncol))
                px, py = q.pop(0)
                board[px][py] = 0
            # 사과가 있다면 이동 후 꼬리 그대로 두기
            elif board[nrow][ncol] == 2:
                board[nrow][ncol] = 1
                q.append((nrow, ncol))
        # 벽이나 몸통에 부딪혔을 경우
        else:
            time += 1
            break
        row, col = nrow, ncol # 다음 머리를 이동
        time += 1
        if index < l and time == info[index][0]: # 회전할 시간인 경우 회전
           if info[index][1] == 'L': # c == 'L'
               direction = (direction - 1) % 4
           else: # c == 'D'
               direction = (direction + 1) % 4
           index += 1
    return time
print(simulate())