d = [0] * 30000
d[1], d[2], d[3], d[4], d[5] = 0, 1, 1, 2, 1

x = int(input())

for i in range(6, x + 1):
    if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
        d[i] = min(d[i - 1], d[i // 2], d[i // 3], d[i // 5]) + 1
    elif i % 2 == 0 and i % 3 == 0:
        d[i] = min(d[i - 1], d[i // 2], d[i // 3]) + 1
    elif i % 2 == 0 and i % 5 == 0:
        d[i] = min(d[i - 1], d[i // 2], d[i // 5]) + 1
    elif i % 3 == 0 and i % 5 == 0:
        d[i] = min(d[i - 1], d[i // 3], d[i // 5]) + 1
    elif i % 5 == 0:
        d[i] = min(d[i - 1], d[i // 5]) + 1
    elif i % 3 == 0:
        d[i] = min(d[i - 1], d[i // 3]) + 1
    elif i % 2 == 0:
        d[i] = min(d[i - 1], d[i // 2]) + 1
    else:
        d[i] = d[i - 1] + 1
print(d[x])