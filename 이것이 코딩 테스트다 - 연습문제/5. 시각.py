count = 0
n = int(input())

for h in range(0, n + 1):
    for m in range(0, 60):
        for s in range(0, 60):
            time = str(h) + str(m) + str(s)
            if '3' in time:
                count += 1
print(count)