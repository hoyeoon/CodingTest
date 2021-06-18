# 오셀로 게임 문제. 백돌은 2로 채워져있고, 흑 돌은 1로 채워져 있음. 빈 칸은 0
# 현재 흑돌 차례. 백돌을 가장 많이 먹을 수 있는 경우의 먹은 개수를 return
# 왜 틀렸지.. 14/100

def solution(board):
    black = [(-2, 0), (0, -2), (2, 0), (0, 2)]
    white = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    n = len(board)
    max_value = -1

    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                result = 0
                for k in range(4):
                    if 0 <= i + black[k][0] < n and 0 <= j + black[k][1] < n:
                        if board[i + black[k][0]][j + black[k][1]] == 1 and board[i + white[k][0]][j + white[k][1]] == 2:
                            result += 1
            max_value = max(max_value, result)


#     # board[6][3]
#     for k in range(4):
#         if 0 <= 6 + black[k][0] < n and 0 <= 3 + black[k][1] < n:
#             print(1)
#             if board[6 + black[k][0]][3 + black[k][1]] == 1 and board[6 + white[k][0]][3 + white[k][1]] == 2:
#                 result += 1

    return max_value