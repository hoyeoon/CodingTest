count = 1
n, m = map(int, input().split())
a, b, d = map(int, input().split())
space = []
for i in range(n):
    space.append(list(map(int, input().split())))

move = [(0, -1), (1, 0), (0, 1), (-1 ,0)]

print(space)
while True:
    if space[b + move[0][1]][a + move[0][0]] == 1 and space[b + move[1][1]][a + move[1][0]] == 1 and space[b + move[2][1]][a + move[2][0]] == 1 and space[b + move[3][1]][a + move[3][0]] == 1:
        if d == 0:
            a = a + move[2][0]
            b = b + move[2][1]
            if space[b][a] == 1:
                break
            continue
        elif d == 1:
            a = a + move[3][0]
            b = b + move[3][1]
            if space[b][a] == 1:
                break
            continue
        elif d == 2:
            a = a + move[0][0]
            b = b + move[0][1]
            if space[b][a] == 1:
                break
            continue
        else:
            a = a + move[1][0]
            b = b + move[1][1]
            if space[b][a] == 1:
                break
            continue
    d = (d - 1) % 4
    if space[b + move[d][1]][a + move[d][0]] == 0:
        space[b][a] = 1
        a = a + move[d][0]
        b = b + move[d][1]
        print(b, a)
        count += 1

print(count)