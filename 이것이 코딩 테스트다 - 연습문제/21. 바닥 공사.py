n = int(input())

d = [0] * 1001
d[1] = 1
d[2] = 3

for i in range(3, n + 1):
    if n % 2 == 0:
        d[i] = d[i - 1] * 2 + 1
    else:
        d[i] = d[i - 1] * 2 - 1
print(d[n] % 796796)