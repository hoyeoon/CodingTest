n, m = map(int, input().split())
l = []
for i in range(n):
    l.append(int(input()))

l.sort()
start = l[0] * 2
d = [-1] * 10001

for i in l:
    d[i] = 1

for i in range(start, m + 1):
    min_value = 10001
    for j in range(n):
        if d[i - l[j]] == -1:
            continue
        elif d[i - l[j]] < min_value:
            min_value = d[i - l[j]]
    if min_value == 10001:
        d[i] = 1
    else:
        d[i] = min_value + 1

print(d)