x, y = 1, 1
n = int(input())
plans = input().split()

# U. D, L. R에 따른 방향
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
moves_types = ['U', 'D', 'L', 'R']

for plan in plans:
    for i in range(len(moves_types)):
        if plan == moves_types[i]:
            nx = x + move[i][0]
            ny = y + move[i][1]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny
print(x, y)