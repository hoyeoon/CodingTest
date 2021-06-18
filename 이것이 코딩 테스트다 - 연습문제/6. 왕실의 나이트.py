count = 0
n = input()
l = list(n)

x = ord(l[0]) - 96
y = int(l[1])

move = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

for i in range(8):
    if 0 < x + move[i][0] < 9 and 0 < y + move[i][1] < 9:
        count += 1
print(count)